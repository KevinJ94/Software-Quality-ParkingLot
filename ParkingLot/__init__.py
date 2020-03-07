from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = '40c76ea5a74e4fe38e7f1138b0464a2f'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost:3306/parkinglot'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 设置这一项是每次请求结束后都会自动提交数据库中的变动
# app.config['SCHEDULER_API_ENABLED '] = True

db = SQLAlchemy(app)
from ParkingLot import routes


