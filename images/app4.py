from datetime import datetime
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
db=SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///sayo.db"
class mayo(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String,nullable=False)
    desc=db.Column(db.String,nullable=False)
    date=db.Column(db.Datetime,default=datetime.utcnow)