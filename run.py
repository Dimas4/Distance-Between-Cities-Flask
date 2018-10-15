from app.create_app import app, db
from routers.routers import *


View.register(app)


if __name__ == '__main__':
    app.run(debug=True)
