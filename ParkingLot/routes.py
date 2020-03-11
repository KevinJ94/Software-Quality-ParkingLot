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
    if user_email:
        #user = User.query.filter_by(email=user_email).first()
        res_list = Reservation.query.join(User).filter(User.email == user_email).all()
        return render_template("index.html", email=user_email, reslist=res_list)
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
        return render_template("index.html")



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
        return render_template("index.html",email = email)



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
        return render_template("index.html",email = email)



# @app.route('/info/', methods=['POST', 'GET'])
# def info_page():
#     group = request.args.get("group")
#     key = request.args.get("key")
#     page = int(request.args.get("page"))
#     avg_rate = int(request.args.get("avg_rate"))
#     if key == '':
#         if group == 'All':
#
#             paginate = Product.query \
#                 .join(Review) \
#                 .filter(Review.avg_rating >= avg_rate) \
#                 .paginate(page, 20, error_out=False)
#         else:
#
#             paginate = Product.query \
#                 .join(Review) \
#                 .filter(Product.group == group) \
#                 .filter(Review.avg_rating >= avg_rate) \
#                 .paginate(page, 20, error_out=False)
#     else:
#         if group == 'All':
#
#             paginate = Product.query \
#                 .join(Review) \
#                 .filter(Product.title.like('%' + key + '%')) \
#                 .filter(Review.avg_rating >= avg_rate) \
#                 .paginate(page, 20, error_out=False)
#         else:
#
#             paginate = Product.query \
#                 .join(Review). \
#                 filter(Product.title.like('%' + key + '%')) \
#                 .filter(Product.group == group) \
#                 .filter(Review.avg_rating >= avg_rate) \
#                 .paginate(page, 20, error_out=False)
#
#     products = paginate.items
#
#     return render_template('information.html', paginate=paginate, products=products, group=group,
#                            key=key, page=page, avg_rate=avg_rate)
#
#
# @app.route('/search', methods=['GET', 'POST'])
# def search_page():
#     data = request.args.to_dict()
#     # form = SearchForm()
#     # if form.validate_on_submit():
#     #     return redirect(url_for('info_page'), code=307)
#     return render_template('search.html', title='Search', result_json=data)
#
#
# @app.route('/detail', methods=['GET'])
# def show_detail():
#     product_id = request.args['product_id']
#
#     product = Product.query.filter_by(Id=product_id).first()
#
#     similars, similar_products = [], []
#
#     for similar in product.similar:
#         similars.append(
#             Product.query.filter_by(ASIN=similar.ASIN).first()
#         )
#
#     for similar in similars:
#         if similar:
#             similar_products.append(similar)
#
#     return render_template('detail.html', product=product, similar_products=similar_products)
#
#
