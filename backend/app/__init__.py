from flask import Config
import os
from flask import Flask, request, g
from flask_cors import CORS
import sqlite3
import random
import datetime


class DefaultConfig(Config):
    TESTING = False
    basedir = os.path.abspath(os.path.dirname(__file__))
    DATABASE = os.path.join(basedir, "backend_database.db")


def create_app_routes(app):
    def get_db():
        db = getattr(g, "_database", None)
        if db is None:
            if app.config["TESTING"] != True:
                g._database = sqlite3.connect(
                    app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
                )
            else:
                # print("Testing DATABASE, so we are doing it in memory!")
                g._database = sqlite3.connect(
                    ":memory:", detect_types=sqlite3.PARSE_DECLTYPES
                )
            db = g._database
            if (
                db.cursor()
                .execute(
                    "SELECT name FROM sqlite_master WHERE type='table' AND name='Users'"
                )
                .fetchone()
                is None
            ):
                with app.open_resource("schema.sql") as f:
                    db.executescript(f.read().decode("utf8"))
                with app.open_resource("seed.sql") as f:
                    db.executescript(f.read().decode("utf8"))
        return db

    def seed_database():
        db = get_db()
        # if the database has nothing in the users, run the seed_database.sql file
        cur = db.cursor()
        cur.execute("SELECT * FROM users")
        output = cur.fetchall()
        if output == []:
            with app.open_resource("seed.sql") as f:
                db.executescript(f.read().decode("utf8"))

    @app.teardown_appcontext
    def close_connection(exception):
        db = getattr(g, "_database", None)
        if db is not None:
            db.close()

    # working hello world route
    @app.route("/")
    def hello_world():
        return "Hello, World!"

    @app.route("/create_user", methods=["POST"])
    def create_user():
        # print("create_user")
        db = get_db()
        cur = db.cursor()
        data = request.get_json()
        # print(data)
        username = data["username"]
        password = data["password"]
        email = data["email"]
        try:
            cur.execute(
                "INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
                (username, password, email),
            )
            db.commit()
        except Exception as e:
            return {"message": "Invalid username or email"}
        return {"message": "User created!"}

    @app.route("/get_users", methods=["GET"])
    def get_users():
        db = get_db()
        cur = db.cursor()
        cur.execute("SELECT * FROM users")
        output = cur.fetchall()
        return {"users": output}

    @app.route("/login_user", methods=["POST"])
    def login_user():
        db = get_db()
        cur = db.cursor()
        data = request.get_json()
        email = data["email"]
        password = data["password"]
        cur.execute(
            "SELECT * FROM users WHERE email = ? AND password = ?", (email, password)
        )
        output = cur.fetchone()
        if output is None:
            return {"message": "User not found"}
        else:
            # if the user exists, pass them a token
            user_token = str(random.randint(0, 1000000))
            # check if the user is already logged in
            if email in app.config["LOGGED_IN_USERS"].values():
                # if they are, delete the old token
                for key in app.config["LOGGED_IN_USERS"].keys():
                    if app.config["LOGGED_IN_USERS"][key] == email:
                        return {"message": "User found", "token": key}
            app.config["LOGGED_IN_USERS"][user_token] = email
            return {"message": "User found", "token": user_token}

    # now whenever a user makes a request, they need to pass their token

    @app.route("/get_user_data", methods=["GET"])
    def get_user_data():
        db = get_db()
        cur = db.cursor()
        token = request.headers.get("token")
        # print(
            # app.config["LOGGED_IN_USERS"],
            # token,
            # token in app.config["LOGGED_IN_USERS"].keys(),
        # )
        if not token in app.config["LOGGED_IN_USERS"].keys():
            return {"message": "User not logged in"}
        email = app.config["LOGGED_IN_USERS"][token]
        cur.execute("SELECT * FROM users WHERE email = ?", (email,))
        output = cur.fetchone()
        return {"user_data": output}

    def get_current_user_id():
        token = request.headers.get("token")
        if not token in app.config["LOGGED_IN_USERS"].keys():
            return None
        db = get_db()
        cur = db.cursor()
        email = app.config["LOGGED_IN_USERS"][token]
        cur.execute("SELECT id FROM users WHERE email = ?", (email,))
        return cur.fetchone()[0]

    @app.route("/create_event", methods=["POST"])
    def create_event():
        user_id = get_current_user_id()
        if user_id is None:
            return {"message": "User not logged in"}
        db = get_db()
        cur = db.cursor()
        data = request.get_json()
        event_name = data["event_name"]
        event_date = data["event_date"]
        event_time = data["event_time"]
        event_description = data["event_description"]
        event_location = data["event_location"]
        # create a datetime object
        event_datetime = datetime.datetime.strptime(
            event_date + " " + event_time, "%Y-%m-%d %H:%M"
        )

        cur.execute(
            "INSERT INTO events (event_name, event_date, user_id, event_description, event_location) VALUES (?, ?, ?, ?, ?)",
            (event_name, event_datetime, user_id, event_description, event_location),
        )

        db.commit()
        return {"message": "Event created!"}

    @app.route("/get_my_events", methods=["GET"])
    def get_my_events():
        user_id = get_current_user_id()
        if user_id is None:
            return {"message": "User not logged in"}
        db = get_db()
        cur = db.cursor()
        cur.execute("SELECT * FROM events WHERE user_id = ?", (user_id,))
        output = cur.fetchall()
        return {"events": output}

    @app.route("/get_event", methods=["GET"])
    def get_event():
        db = get_db()
        cur = db.cursor()
        event_id = request.args.get("event_id")
        cur.execute("SELECT * FROM events WHERE id = ?", (event_id,))
        output = cur.fetchone()
        return {"event": output}

    @app.route("/reset_password", methods=["POST"])
    def reset_password():
        """
        This is for a user that is already logged in, and they are using their old and new password
        to change the password.
        """

        user_id = get_current_user_id()
        if user_id is None:
            return {"message": "User not logged in"}

        db = get_db()
        cur = db.cursor()
        data = request.get_json()
        old_password = data["old_password"]
        new_password = data["new_password"]
        cur.execute("SELECT * FROM Users WHERE id = ?", (user_id,))
        output = cur.fetchone()
        if output is None:
            return {"message": "User not found"}

        if output[2] != old_password:
            return {"message": "Old password incorrect"}

        cur.execute(
            "UPDATE Users SET password = ? WHERE id = ?", (new_password, user_id)
        )
        db.commit()

        return {"message": "Password updated!"}

    @app.route("/rsvp_to_event", methods=["POST"])
    def rsvp_to_event():
        user_id = get_current_user_id()
        if user_id is None:
            return {"message": "User not logged in"}
        db = get_db()
        cur = db.cursor()
        data = request.get_json()
        event_id = data["event_id"]
        cur.execute(
            "INSERT INTO rsvps (user_id, event_id) VALUES (?, ?)",
            (user_id, event_id),
        )
        db.commit()
        return {"message": "RSVP created!"}

    @app.route("/unrsvp_to_event", methods=["POST"])
    def unrsvp_to_event():
        user_id = get_current_user_id()
        if user_id is None:
            return {"message": "User not logged in"}
        db = get_db()
        cur = db.cursor()
        data = request.get_json()
        event_id = data["event_id"]
        cur.execute(
            "DELETE FROM rsvps WHERE user_id = ? AND event_id = ?",
            (user_id, event_id),
        )
        db.commit()
        return {"message": "RSVP deleted!"}

    @app.route("/get_rsvps", methods=["GET"])
    def get_rsvps():
        db = get_db()
        cur = db.cursor()
        event_id = request.args.get("event_id")
        cur.execute("SELECT * FROM rsvps WHERE event_id = ?", (event_id,))
        output = cur.fetchall()
        return {"rsvps": output}

    @app.route("/add_food", methods=["POST"])
    def add_food():
        user_id = get_current_user_id()
        if user_id is None:
            return {"message": "User not logged in"}
        db = get_db()
        cur = db.cursor()
        data = request.get_json()
        food_event = data["event_id"]
        food_name = data["food_name"]
        food_servings = data["servings"]

        # make sure there is a valid rsvp for this user and event
        cur.execute(
            "SELECT * FROM rsvps WHERE user_id = ? AND event_id = ?",
            (user_id, food_event),
        )
        output = cur.fetchone()
        if output is None:
            return {"message": "User not RSVP'd to this event"}

        cur.execute(
            "INSERT INTO food (event_id, rsvp_id, food_name, servings) VALUES (?, ?, ?, ?)",
            (food_event, output[0], food_name, food_servings),
        )
        db.commit()

        return {"message": "Food created!"}

    @app.route("/get_foods_for_event", methods=["GET"])
    def get_foods_for_event():
        db = get_db()
        cur = db.cursor()
        event_id = request.args.get("event_id")
        cur.execute(
            """SELECT food.event_id, food.rsvp_id, food.recipe_id, food.food_name, food.servings, users.id, users.email, food.id  FROM food
    INNER JOIN rsvps ON food.rsvp_id = rsvps.id
    INNER JOIN users ON rsvps.user_id = users.id
    WHERE food.event_id = ?""",
            (event_id,),
        )
        output = cur.fetchall()
        return {"foods": output}

    @app.route("/owner_remove_food_from_event", methods=["POST"])
    def owner_remove_food_from_event():
        user_id = get_current_user_id()
        if user_id is None:
            return {"message": "User not logged in"}
        db = get_db()
        cur = db.cursor()
        data = request.get_json()

        food_id = data["food_id"]
        event_id = data["event_id"]

        # make sure the user owns the event
        cur.execute(
            "SELECT * FROM events WHERE id = ? AND user_id = ?", (event_id, user_id)
        )
        output = cur.fetchone()
        if output is None:
            return {"message": "User does not own this event"}

        cur.execute("DELETE FROM food WHERE id = ?", (food_id,))
        db.commit()

        return {"message": "Food deleted!"}

    @app.route("/owner_remove_rsvp_from_event", methods=["POST"])
    def owner_remove_rsvp_from_event():
        user_id = get_current_user_id()
        if user_id is None:
            return {"message": "User not logged in"}
        db = get_db()
        cur = db.cursor()
        data = request.get_json()

        rsvp_id = data["rsvp_id"]
        event_id = data["event_id"]

        # make sure the user owns the event
        cur.execute(
            "SELECT * FROM events WHERE id = ? AND user_id = ?", (event_id, user_id)
        )
        output = cur.fetchone()
        if output is None:
            return {"message": "User does not own this event"}

        cur.execute("DELETE FROM rsvps WHERE id = ?", (rsvp_id,))
        db.commit()

        return {"message": "RSVP deleted!"}

    @app.route("/edit_event", methods=["POST"])
    def edit_event():
        user_id = get_current_user_id()
        if user_id is None:
            return {"message": "User not logged in"}
        db = get_db()
        cur = db.cursor()
        data = request.get_json()
        event_id = data["event_id"]
        event_name = data["event_name"]
        event_date = data["event_date"]
        event_time = data["event_time"]
        event_description = data["event_description"]
        event_location = data["event_location"]
        # create a datetime object
        event_datetime = datetime.datetime.strptime(
            event_date + " " + event_time, "%Y-%m-%d %H:%M"
        )

        # make sure the user owns the event
        cur.execute(
            "SELECT * FROM events WHERE id = ? AND user_id = ?", (event_id, user_id)
        )
        output = cur.fetchone()
        if output is None:
            return {"message": "User does not own this event"}

        cur.execute(
            "UPDATE events SET event_name = ?, event_date = ?, event_description = ?, event_location = ? WHERE id = ?",
            (event_name, event_datetime, event_description, event_location, event_id),
        )

        db.commit()
        return {"message": "Event updated!"}

    @app.route("/get_my_rsvps", methods=["GET"])
    def get_my_rsvps():
        user_id = get_current_user_id()
        if user_id is None:
            return {"message": "User not logged in"}
        db = get_db()
        cur = db.cursor()
        cur.execute("SELECT * FROM rsvps WHERE user_id = ?", (user_id,))
        output = cur.fetchall()

        # get a list of events from the rsvps
        events = []
        for rsvp in output:
            cur.execute("SELECT * FROM events WHERE id = ?", (rsvp[2],))
            events.append(cur.fetchone())

        return {"events": events}

    @app.route("/check_if_rsvpd", methods=["GET"])
    def check_if_rsvpd():
        user_id = get_current_user_id()
        if user_id is None:
            return {"message": "User not logged in"}
        db = get_db()
        cur = db.cursor()
        event_id = request.args.get("id")
        cur.execute(
            "SELECT * FROM rsvps WHERE user_id = ? AND event_id = ?",
            (user_id, event_id),
        )
        output = cur.fetchone()
        if output is None:
            return {"rsvpd": False}
        else:
            return {"rsvpd": True}

    @app.route("/get_food", methods=["GET"])
    def get_food():
        db = get_db()
        cur = db.cursor()
        food_id = request.args.get("food_id")
        cur.execute("SELECT * FROM food WHERE id = ?", (food_id,))
        output = cur.fetchone()
        return {"food": output}

    @app.route("/edit_food", methods=["POST"])
    def edit_food():
        user_id = get_current_user_id()
        if user_id is None:
            return {"message": "User not logged in"}
        db = get_db()
        cur = db.cursor()
        data = request.get_json()
        food_id = data["food_id"]
        food_name = data["food_name"]
        food_servings = data["servings"]

        # make sure the user owns the food
        cur.execute(
            "SELECT * FROM food INNER JOIN rsvps ON food.rsvp_id = rsvps.id INNER JOIN users ON rsvps.user_id = users.id WHERE food.id = ? AND users.id = ?",
            (food_id, user_id),
        )
        output = cur.fetchone()
        if output is None:
            return {"message": "User does not own this food"}

        cur.execute(
            "UPDATE food SET food_name = ?, servings = ? WHERE id = ?",
            (food_name, food_servings, food_id),
        )
        db.commit()
        return {"message": "Food updated!"}

    @app.route("/delete_event", methods=["POST"])
    def delete_event():
        user_id = get_current_user_id()
        if user_id is None:
            return {"message": "User not logged in"}
        db = get_db()
        cur = db.cursor()
        data = request.get_json()
        event_id = data["event_id"]
        cur.execute(
            "DELETE FROM events WHERE id = ? AND user_id = ?", (event_id, user_id)
        )
        db.commit()
        return {"message": "Event deleted!"}

    @app.route("/delete_food", methods=["POST"])
    def delete_food():
        user_id = get_current_user_id()
        if user_id is None:
            return {"message": "User not logged in"}
        db = get_db()
        cur = db.cursor()
        data = request.get_json()
        food_id = data["food_id"]
        cur.execute("DELETE FROM food WHERE id = ?", (food_id,))
        db.commit()
        return {"message": "Food deleted!"}


def create_app(config_class=DefaultConfig):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_class)
    app.config["LOGGED_IN_USERS"] = {}
    # print("Server Initialized!")
    create_app_routes(app)
    return app


if __name__ == "__main__":
    app = create_app()
