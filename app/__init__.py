from flask import Flask
from .db import db, migrate
from .models import cat, dog, caretaker
from .routes.cat_routes import bp as cats_bp
from .routes.dog_routes import bp as dogs_bp
from .routes.caretaker_routes import bp as caretakers_bp
import os

def create_app(config=None):
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

    if config:
        # Merge `config` into the app's configuration
        # to override the app's default settings
        app.config.update(config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(cats_bp)
    app.register_blueprint(dogs_bp)
    app.register_blueprint(caretakers_bp)

    return app