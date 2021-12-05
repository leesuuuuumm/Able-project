from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
# from .config import config_by_name
from datetime import timedelta

# db = SQLAlchemy()
flask_bcrypt = Bcrypt()
login = LoginManager()


def create_app(config_name):
	app = Flask(__name__)
	app.debug = True
	app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
	app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=5)
	# app.config.from_object(config_by_name[config_name])
	# db.init_app(app)
	flask_bcrypt.init_app(app)
	# login.blueprint_login_views = {
	# 	'user_route': 'user_route.login',
	# 	'admin_route': 'admin_route.login'
	# }
	#
	# login.init_app(app)

	return app