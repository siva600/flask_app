# this module initializes and collects everything that are needed for our app.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# instantiating the flask application with app variable.

app = Flask(__name__)
app.config['SECRET_KEY'] = 'e4600f6c32fbba96678367ac5402bb34'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
# passing the app to initialize that
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
from app import routes
