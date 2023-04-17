from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy()
db.init_app(app)

migrate = Migrate(app, db)


@app.route("/")
def index():
    return "Welcome to the propagation station API!"


if __name__ == "__main__":
    app.run()

import models
