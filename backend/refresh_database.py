import sqlite3

if __name__ == "__main__":
    # get the database
    db = sqlite3.connect("./backend_database.db")

    # drop all tables
    db.execute("DROP TABLE IF EXISTS Users")
    db.execute("DROP TABLE IF EXISTS Events")
    db.commit()

    # open the "schema.sql" file
    with open("schema.sql") as f:
        db.executescript(f.read())

    # close the database
    db.close()
