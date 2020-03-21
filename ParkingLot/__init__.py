from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_monitoringdashboard as dashboard

app = Flask(__name__)
dashboard.config.init_from(file='config.cfg')
dashboard.bind(app)
app.config['SECRET_KEY'] = '40c76ea5a74e4fe38e7f1138b0464a2f'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:china666@localhost:3306/parkinglot'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 设置这一项是每次请求结束后都会自动提交数据库中的变动

app.config['SQLALCHEMY_RECORD_QUERIES  '] = True
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 90
app.config['SQLALCHEMY_POOL_SIZE'] = 1024
app.config['SQLALCHEMY_POOL_RECYCLE'] = 3
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 1024


db = SQLAlchemy(app)

from ParkingLot import routes


