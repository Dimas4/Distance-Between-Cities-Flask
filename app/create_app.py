import yaml

from flask_sqlalchemy import SQLAlchemy
from flask import Flask


def create_app(config):
    db_config = config['database']
    app = Flask(__name__, template_folder='../templates')
    app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f"{db_config['type']}://{db_config['username']}:{db_config['password']}" \
                                            f"@{db_config['host']}/{db_config['db_name']}"
    db = SQLAlchemy(app)
    return app, db


with open('config.yaml', 'r') as file:
    config = yaml.load(file)

app, db = create_app(config)
