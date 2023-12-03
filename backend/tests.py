from flask import Config
from app import create_app
import unittest
import os


class TestConfig(Config):
    TESTING = True
    basedir = os.path.abspath(os.path.dirname(__file__))
    DATABASE = os.path.join(basedir, "../testing_database.db")
    FLASK_APP = "main.py"


class ServerTests(unittest.TestCase):
    def client(self):
        return self.app.test_client()

    def setUp(self):
        self.app = create_app(TestConfig)

    def tearDown(self):
        pass

    def login(self):
        response = self.client().post(
            "/login_user",
            json={"email": "adalovelace@example.com", "password": "adalovelace"},
        )
        # print(response)
        return response.json["token"]

    def test_home(self):
        response = self.client().get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Hello, World!")

    def test_signup(self):
        """
        @app.route("/create_user", methods=["POST"])
        def create_user():
            print("create_user")
            db = get_db()
            cur = db.cursor()
            data = request.get_json()
            print(data)
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
        """
        response = self.client().post(
            "/create_user",
            json={
                "username": "test",
                "password": "test",
                "email": "test@example.com",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "User created!"})

    def test_login(self):
        """
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
        """
        response = self.client().post(
            "/login_user",
            json={"email": "adalovelace@example.com", "password": "adalovelace"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["message"], "User found")
        self.assertIsNotNone(response.json["token"])

    def test_create_event(self):
        """
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
        """
        # first log in as a user to get a token
        token = self.login()

        # then create an event
        response = self.client().post(
            "/create_event",
            json={
                "event_name": "test",
                "event_date": "2021-01-01",
                "event_time": "12:00",
                "event_description": "test",
                "event_location": "test",
            },
            headers={"token": token},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["message"], "Event created!")

    def test_get_events(self):
        """
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
        """
        # first log in as a user to get a token
        token = self.login()

        # then create an event
        response = self.client().get("/get_my_events", headers={"token": token})
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json["events"])

    def test_get_user_data(self):
        """
        @app.route("/get_user_data", methods=["GET"])
        def get_user_data():
            db = get_db()
            cur = db.cursor()
            token = request.headers.get("token")
            print(
                app.config["LOGGED_IN_USERS"],
                token,
                token in app.config["LOGGED_IN_USERS"].keys(),
            )
            if not token in app.config["LOGGED_IN_USERS"].keys():
                return {"message": "User not logged in"}
            email = app.config["LOGGED_IN_USERS"][token]
            cur.execute("SELECT * FROM users WHERE email = ?", (email,))
            output = cur.fetchone()
            return {"user_data": output}
        """
        # first log in as a user to get a token
        token = self.login()

        # then create an event
        response = self.client().get("/get_user_data", headers={"token": token})
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json["user_data"])

    def test_get_event(self):
        """
        @app.route("/get_event", methods=["GET"])
        def get_event():
            db = get_db()
            cur = db.cursor()
            event_id = request.args.get("event_id")
            cur.execute("SELECT * FROM events WHERE id = ?", (event_id,))
            output = cur.fetchone()
            return {"event": output}
        """
        # first log in as a user to get a token
        token = self.login()

        # then create an event
        response = self.client().get("/get_event?event_id=1", headers={"token": token})
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json["event"])

    def test_reset_password(self):
        """
        @app.route("/reset_password", methods=["post"])
        def reset_password():
            \"\"\"
            this is for a user that is already logged in, and they are using their old and new password
            to change the password.
            \"\"\"

            user_id = get_current_user_id()
            if user_id is none:
                return {"message": "user not logged in"}

            db = get_db()
            cur = db.cursor()
            data = request.get_json()
            old_password = data["old_password"]
            new_password = data["new_password"]
            cur.execute("select * from users where id = ?", (user_id,))
            output = cur.fetchone()
            if output is none:
                return {"message": "user not found"}

            if output[2] != old_password:
                return {"message": "old password incorrect"}

            cur.execute("update users set password = ? where id = ?", (new_password, user_id))
            db.commit()

            return {"message": "Password updated!"}
        """
        # first log in as a user to get a token
        token = self.login()

        # then create an event
        response = self.client().post(
            "/reset_password",
            json={"old_password": "adalovelace", "new_password": "adalovelace"},
            headers={"token": token},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["message"], "Password updated!")

    def test_rsvp_to_event(self):
        """
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
        """
        # first log in as a user to get a token
        token = self.login()

        # then create an event
        response = self.client().post(
            "/rsvp_to_event",
            json={"event_id": 2},
            headers={"token": token},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["message"], "RSVP created!")

    def test_unrsvp_to_event(self):
        """
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
        """
        # first log in as a user to get a token
        token = self.login()

        # then create an event
        response = self.client().post(
            "/unrsvp_to_event",
            json={"event_id": 1},
            headers={"token": token},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["message"], "RSVP deleted!")

    def test_get_rsvps(self):
        """
        @app.route("/get_rsvps", methods=["GET"])
        def get_rsvps():
            db = get_db()
            cur = db.cursor()
            event_id = request.args.get("event_id")
            cur.execute("SELECT * FROM rsvps WHERE event_id = ?", (event_id,))
            output = cur.fetchall()
            return {"rsvps": output}
        """
        # first log in as a user to get a token
        token = self.login()

        # then create an event
        response = self.client().get("/get_rsvps?event_id=1", headers={"token": token})
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json["rsvps"])

    def test_add_food(self):
        """
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
                "SELECT * FROM rsvps WHERE user_id = ? AND event_id = ?", (user_id, food_event)
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
        """
        # first log in as a user to get a token
        token = self.login()

        # then create an event
        response = self.client().post(
            "/add_food",
            json={"event_id": 1, "food_name": "test", "servings": 1},
            headers={"token": token},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["message"], "Food created!")

    def test_get_foods_for_event(self):
        """
        @app.route("/get_foods_for_event", methods=["GET"])
        def get_foods_for_event():
            db = get_db()
            cur = db.cursor()
            event_id = request.args.get("event_id")
            cur.execute(
                \"\"\"SELECT food.event_id, food.rsvp_id, food.recipe_id, food.food_name, food.servings, users.id, users.email, food.id  FROM food
        INNER JOIN rsvps ON food.rsvp_id = rsvps.id
        INNER JOIN users ON rsvps.user_id = users.id
        WHERE food.event_id = ?\"\"\",
                (event_id,),
            )
            output = cur.fetchall()
            return {"foods": output}
        """
        # first log in as a user to get a token
        token = self.login()

        # then create an event
        response = self.client().get(
            "/get_foods_for_event?event_id=1", headers={"token": token}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json["foods"])

    def test_check_if_rsvpd(self):
        """
        @app.route("/check_if_rsvpd", methods=["GET"])
        def check_if_rsvpd():
            user_id = get_current_user_id()
            if user_id is None:
                return {"message": "User not logged in"}
            db = get_db()
            cur = db.cursor()
            event_id = request.args.get("id")
            cur.execute(
                "SELECT * FROM rsvps WHERE user_id = ? AND event_id = ?", (user_id, event_id)
            )
            output = cur.fetchone()
            if output is None:
                return {"rsvpd": False}
            else:
                return {"rsvpd": True}
        """
        # first log in as a user to get a token
        token = self.login()

        # then check if rsvpd
        response = self.client().get("/check_if_rsvpd?id=3", headers={"token": token})
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json["rsvpd"])


if __name__ == "__main__":
    # remove 'test_database'
    unittest.main()
