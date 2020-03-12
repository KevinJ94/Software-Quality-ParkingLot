import json
import random

from flask import render_template, url_for, redirect, request, session
from ParkingLot import app, db
from ParkingLot.models import *


# @app.before_request
# def before():
#     if request.path == '/login':
#         return None
#     if request.path == '/checklogin':
#         return None
#     if request.path == '/reg':
#         return None
#     email = request.args.get("email")
#     if email:
#         user = session.get(email)
#         if user:
#             return None
#     return redirect("/login")


@app.route('/')
def root():
    user_email = session.get(request.args.get("email"))
    user = User.query.filter_by(email=user_email).first()
    if user_email:
        res_list = Reservation.query.join(User).filter(User.email == user_email).all()
        can_res = True
        for res in res_list:
            if res.status == "Confirmed":
                can_res = False
                break
        return render_template("index.html", email=user_email, reslist=res_list,user =user,canres = can_res)
    else:
        return render_template("login.html")


@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/logout')
def logout():
    session.clear()
    return render_template("login.html")


@app.route('/checklogin', methods=['POST'])
def checklogin():
    email = request.form.get("email")
    password = request.form.get("password")
    user = User.query.filter_by(email=email).first()

    if user.password == password:
        session[user.email] = user.email
        return redirect("/?email=" + user.email)
    else:
        return redirect("/login")


@app.route('/reg', methods=['GET', 'POST'])
def reg():
    if request.method == "GET":
        return render_template("reg.html")
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User()
        user.email = email
        user.password = password
        user.type = '0'
        user.isArrive = 0
        print(user.email, user.password, user.type)
        try:
            db.session.add(user)
            db.session.commit()
            return redirect("/login")
        except:
            return redirect("/reg")


@app.route('/makeRes', methods=['GET', 'POST'])
def makeReservation():
    if request.method == "GET":
        email = request.args.get("email")
        return render_template("makeReservation.html",email=email)
    if request.method == "POST":
        email = request.form.get("email")
        start = request.form.get("start")
        end = request.form.get("end")
        user = User.query.filter_by(email=email).first()
        res = Reservation()
        res.user = user
        res.startTime = start
        res.endTime = end
        res.status = "Confirmed"
        res.type = "Normal"
        res.confirmNum = random.randint(0,1000)
        db.session.add(res)
        db.session.commit()
        return redirect("/?email=" + user.email)



@app.route('/transaction', methods=['GET', 'POST'])
def transaction():
    return render_template("transaction.html")


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == "GET":

        email = request.args.get("email")
        user = User.query.filter_by(email=email).first()
        profile = Profile.query.filter_by(userId=user.id).first()
        profile.birthday = profile.birthday.strftime("%Y-%m-%d")

        return render_template("profile.html", email=email , profile= profile)

    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        birthday = request.form.get("birthday")
        user = User.query.filter_by(email=email).first()
        profile = Profile.query.filter_by(userId=user.id).first()
        if profile:
            profile.user = user
            profile.email = email
            profile.name = name
            profile.birthday = birthday
            db.session.commit()
        else:
            profile = Profile()
            profile.user = user
            profile.email = email
            profile.name = name
            profile.birthday = birthday
            db.session.add(profile)
            db.session.commit()
        return redirect("/?email=" + user.email)



@app.route('/plate', methods=['GET', 'POST'])
def plate():
    if request.method == "GET":

        email = request.args.get("email")
        user = User.query.filter_by(email=email).first()
        plate = Plate.query.filter_by(userId=user.id).first()
        return render_template("plate.html", email=email , plate= plate)

    if request.method == "POST":
        email = request.form.get("email")
        plate_num = request.form.get("plateNum")
        user = User.query.filter_by(email=email).first()
        plate = Plate.query.filter_by(userId=user.id).first()
        if plate:
            plate.plateNumber = plate_num
            plate.userId = user.id
            db.session.commit()
        else:
            plate = Plate()
            plate.plateNumber = plate_num
            plate.userId = user.id
            db.session.add(plate)
            db.session.commit()
        return redirect("/?email=" + user.email)

@app.route('/cancel', methods=['GET', 'POST'])
def cancel():
    email = request.args.get("email")
    res_id = request.args.get("resid")
    res = Reservation.query.filter_by(id=res_id).first()
    res.status = "Canceled"
    db.session.commit()
    return redirect("/?email="+email)

@app.route('/arrive', methods=['GET', 'POST'])
def arrive():
    email = request.args.get("email")
    user = User.query.filter_by(email=email).first()
    user.isArrive = 1
    db.session.commit()
    return redirect("/?email="+email)

@app.route('/depart', methods=['GET', 'POST'])
def depart():
    email = request.args.get("email")
    user = User.query.filter_by(email=email).first()
    user.isArrive = 0
    db.session.commit()
    return redirect("/?email="+email)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    user_email = session.get(request.args.get("email"))
    user = User.query.filter_by(email=user_email).first()
    if user_email:
        return render_template("admin.html", email=user_email)
    else:
        return render_template("admin_login.html")


@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == "GET":
        return render_template("admin_login.html")
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        print(email,password)
        user = User.query.filter_by(email=email).first()

        if user.password == password and user.type == '1':
            session[user.email] = user.email
            return redirect("/admin?email=" + user.email)
        else:
            return redirect("/admin_login")

@app.route('/admin_logout')
def admin_logout():
    session.clear()
    return render_template("login.html")

@app.route('/spots', methods=['GET', 'POST'])
def spots():
    if request.method == "GET":
        return render_template("spots.html")
    if request.method == "POST":
        pass