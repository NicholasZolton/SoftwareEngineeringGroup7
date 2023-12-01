import sqlite3

if __name__ == "__main__":
    # get the database
    db = sqlite3.connect("./backend_database.db")

    # drop all tables
    db.execute("DROP TABLE IF EXISTS Users")
    db.execute("DROP TABLE IF EXISTS Events")
    db.execute("DROP TABLE IF EXISTS Recipe")
    db.execute("DROP TABLE IF EXISTS Allergies")
    db.execute("DROP TABLE IF EXISTS RSVPs")
    db.execute("DROP TABLE IF EXISTS Food")
    db.commit()

    # open the "schema.sql" file
    with open("./schema.sql") as f:
        db.executescript(f.read())

    # seed the database
    with open("./seed.sql") as f:
        db.executescript(f.read())

    # close the database
    db.close()
