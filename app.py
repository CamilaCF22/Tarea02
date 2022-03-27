from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from utils.db import db

app = Flask(__name__)

app.config.from_object("config.BaseConfig")

SQLAlchemy(app)

app.register_blueprint(country)
app.register_blueprint(countrymessages)

