from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

def mkpath(p):
    return os.path.normpath(os.path.join(os.path.dirname(__file__), p))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + mkpath('../quiz.db')
app.config["SQLALCHEMY_ECHO"] = True 

db = SQLAlchemy(app)