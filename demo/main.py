import os
from flask import Flask
from flask_sqlalchemy import  SQLAlchemy
import pymysql
from flask_wtf import CSRFProtect
from flask_restful import Api
from flask_migrate import Migrate
pymysql.install_as_MySQLdb()



app = Flask(__name__)
app.config.from_pyfile("settings.py")
app.config.from_object("settings.Config")
# BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.secret_key = "123123"
models = SQLAlchemy(app)
csrf=CSRFProtect(app)
api = Api(app)
migrate = Migrate(app,models)


#
# # app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///"+os.path.join(BASE_DIR,"ORM.sqlite")
# app.config["SQLALCHEMY_DATABASE_URI"]="mysql://root:111111@localhost/demo1"
#
#
# app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
# app.config["SQLALCHEMY_RTACK_MODIFICATIONS"] = True
# models = SQLAlchemy(app)