import os, json


from flask import Flask, session, render_template, request, redirect, url_for, flash
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


app.static_folder = 'static'

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
                    app.config["SECRET_KEY"]="secretkey"
                    session["USERNAME"]= p_username
                    return render_template("dashboard.html")


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


wordlist=["dog", "cat", "run"]

for i in wordlist:
    getword = i

globalvar = getword


@app.route("/start", methods=["GET","POST"])
def start():

    if request.method=="GET":


        word = request.form.get("word")


        return render_template("game.html", word=getword)



    else:

        word = request.form.get("word")


        if word==getword:
                message="Great job!"
                #return redirect(url_for('start'))
                return render_template("checkvoice.html", message=message, points="1")
        else:
                message="Sorry, incorrect."
                #return redirect(url_for('start'))
                return render_template("checkvoice.html", message=message, points="2")


@app.route("/checkvoice", methods=["GET","POST"])
def checkvoice():



    if request.method=="POST":
        speak = request.form.get("speak")

        return render_template("checkvoice.html")



    else:
        speak = request.form.get("speak")


        if str(speak)==globalvar:


            return redirect(url_for("start2"))
        else:



            return redirect(url_for("start3"))






@app.route("/start2", methods=["GET","POST"])
def start2():

    if request.method=="GET":


        word = request.form.get("word")
        getword = "mouse"


        return render_template("game.html", word=getword, points="2")



    else:
        return redirect(url_for("start3"))
        message="Sorry, incorrect."
        return render_template("message.html", printthis=message)




@app.route("/start3", methods=["GET","POST"])
def start3():

    if request.method=="GET":


        word = request.form.get("word")
        getword = "book"


        return render_template("game.html", word=getword, points="2")



    else:

        word = request.form.get("word")


        if word=="book":
            message=" job!"

            return render_template("checkvoice.html", message=message, points= "2")
        else:
            message=" job!"

            return render_template("checkvoice.html", message=message, points= "2")










@app.route("/sentence", methods=["GET","POST"])
def sentence():
    sentence = "The quick brown fox jumps over the lazy dog"
    return render_template("sentence.html", printthis=sentence)

@app.route("/sentence2", methods=["GET","POST"])
def sentence2():
    sentence = "The dog chases the fat cat"
    return render_template("sentence.html", printthis=sentence)


@app.route("/grammar",  methods=["GET","POST"])
def grammar():
    return render_template("grammar.html")
