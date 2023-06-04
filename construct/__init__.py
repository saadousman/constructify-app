from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from flask_login import LoginManager
from datetime import date, timedelta
from flask_mail import Mail, Message

#All application configurations

#Flask configurations
app = Flask(__name__)
app.secret_key = 'df068fc9da4421a70764842f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///construct.db'
#Configurations for the email library
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'sdousmanflask@gmail.com'
app.config['MAIL_PASSWORD'] = 'Redbull12!123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
#configurations for the sqlalchemy db
db = SQLAlchemy(app)
db.create_all()
#configs for uploads
UPLOAD_FOLDER = 'construct/static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
bcrypt = Bcrypt(app)
#configurations for user session management
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
mail= Mail(app)






from construct import routes