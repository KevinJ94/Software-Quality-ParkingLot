import json
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
    return render_template("index.html", email=user_email)


@app.route('/login')
def login():
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


@app.route('/makeReservation', methods=['GET', 'POST'])
def makeReservation():
    pass


@app.route('/reservation', methods=['GET', 'POST'])
def reservation():
    return redirect("/?email=" + user.email)


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    return redirect("/?email=" + user.email)


@app.route('/plate', methods=['GET', 'POST'])
def plate():
    return redirect("/?email=" + user.email)



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
