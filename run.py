import yaml

from app.create_app import app, db
from routers.routers import *


with open('config.yaml', 'r') as file:
    config = yaml.load(file)['api']


if __name__ == '__main__':
    app.run(debug=True)
