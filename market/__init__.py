

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '66aba279aa67069383d8acac'
db = SQLAlchemy(app)
app.app_context().push()
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page" #a config for login_required to say where our login route is located(passing it in as a string)
login_manager.login_message_category = "info"

from market import routes

