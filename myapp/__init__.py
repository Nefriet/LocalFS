from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'myapp/static/uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///filebase.db'
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev') #For custom secret_key use: "export SECRET_KEY='your-secret-key'" else it will be default 'dev'
db = SQLAlchemy(app)
migrate = Migrate(app,db)

from myapp import routes, models