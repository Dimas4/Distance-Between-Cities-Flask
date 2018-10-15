from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__, template_folder='../templates')
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ivan:ivanivan@localhost/flasknew'
db = SQLAlchemy(app)
