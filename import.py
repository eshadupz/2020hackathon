import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(("postgres://raqviypsgubyrc:aa5f30d241a846eb1ecdd3301c213c1d033d26e7ca94337af49d5ddb6c9232a7@ec2-34-197-188-147.compute-1.amazonaws.com:5432/d3qua3pld2230l")) #if doesnt work replace with actual url
db = scoped_session(sessionmaker(bind=engine))

def main():
    db.execute("DROP TABLE IF EXISTS words")
    db.execute("CREATE TABLE words (id SERIAL PRIMARY KEY, word VARCHAR NOT NULL)")

    db.execute("CREATE TABLE users (user_id SERIAL PRIMARY KEY, username VARCHAR NOT NULL, password VARCHAR NOT NULL)")

    w = open("words.csv")
    reader = csv.reader(w)
    for word in reader:
        db.execute("INSERT INTO words (word) VALUES (:word)",
                {"word":word})
        print("Added")
    db.commit()

if __name__ == "__main__":
    main()
