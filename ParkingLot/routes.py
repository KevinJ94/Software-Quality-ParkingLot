from flask import render_template, url_for, redirect, request
from ParkingLot import app
from ParkingLot import db
from ParkingLot.models import *



@app.route('/')
def root():
    return "Hello World"


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
