from app import app, db
from flask import render_template, request, session, redirect
from models.models import Plant, User
from sqlalchemy import or_
import hashlib


@app.route("/")
def main():
    plants = Plant.query.order_by(Plant.title.asc()).all()
    user = None
    if session.get("user", False):
        user = User.query.get(session.get("user"))
    return render_template("index.html", plants=plants, user=user)


@app.route("/sign-up", methods=["POST", "GET"])
def sign_up():
    if request.method == "POST":
        data = request.form
        user_email = User.query.filter(User.email == request.form.get("email")).first()
        if user_email is not None:
            email_auth = True
            return render_template("sign-up.html", email_auth=email_auth)
        elif data.get("password")=="":
            pass_auth = True
            return render_template("sign-up.html", pass_auth=pass_auth)
        elif data.get("username")=="":
            user_auth = True
            return render_template("sign-up.html", user_auth=user_auth)
        else:
            user = User(
                username=data.get("username"),
                email=data.get("email"),
                password=hashlib.md5(data.get("password").encode()).hexdigest(),
                first_name=data.get("first_name"),
                last_name=data.get("last_name")
            )
        db.session.add(user)
        db.session.commit()
        session["user"] = user.id
        return redirect("/")
    else:
        return render_template("sign-up.html")


@app.route("/sign-in", methods=["POST", "GET"])
def sign_in():
    if request.method == "POST":
        user = User.query.filter(or_(User.email == request.form.get("email"), User.username == request.form.get("email"))).first()
        if user is not None:
            print("hasshes")
            print(user.password)
            print(hashlib.md5(request.form.get("password").encode()).hexdigest())
            if user.password == hashlib.md5(request.form.get("password").encode()).hexdigest():
                session["user"] = user.id
        return redirect("/")
    else:
        return render_template("sign-in.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")