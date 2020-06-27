import os, json


from flask import Flask, session, render_template, request, redirect, url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from datetime import timedelta


app = Flask(__name__)
app.config["SECRET_KEY"]="secretkey"


if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")


app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


app=Flask(__name__)

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method=="POST":
        username = request.form.get("username")
        password = request.form.get("password")

        db.execute("INSERT INTO users (username, password) VALUES (:username, :password)",
                        {"username": username, "password": password})
        db.commit()

        return render_template("register.html")
    else:
        return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
     if request.method == "POST":
            p_username = request.form.get("username")
            p_password = request.form.get("password")


            checkuser = db.execute("SELECT username FROM users WHERE username=:username;", {"username": p_username}).fetchone()

            if checkuser is not None:

                checkpass = db.execute("SELECT username FROM users WHERE password=:password AND username=:username;", {"password": p_password, "username": p_username}).fetchone()

                if checkpass is not None:

                    #return render_template("success.html", printthis = "You are logged in", name = p_username)
                    session["USERNAME"]= p_username
                    return render_template("search.html")


                else:
                    return render_template("message.html", printthis = "User or pass not correct")

            else:
                return render_template("message.html", printthis="This user does not exist")

     else:
         return render_template("login.html")
db.commit()


@app.route("/", methods=["GET","POST"])
def main():
    return render_template("index.html")


@app.route("/index", methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/dashboard", methods=["GET","POST"])
def dashboard():
    return render_template("dashboard.html")



getword = db.execute("SELECT word FROM words").fetchone()

@app.route("/start", methods=["GET","POST"])
def start():

    if request.method=="GET":

        word = request.form.get("word")


        return render_template("game.html", word=getword)



    else:
        word = request.form.get("word")
        if word==getword:
            return render_template("message.html", message="Good job!")
            return redirect(url_for('checkvoice'))
        else:
        #    return render_template("message.html", message="Incorrect.")
            return redirect(url_for('checkvoice'))

@app.route("/checkvoice", methods=["GET","POST"])
def checkvoice():
    return render_template("checkvoice.html")
    speak = request.form.get("speak")
