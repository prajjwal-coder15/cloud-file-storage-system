from flask import Flask
from .extension import mongo, login_manager
from .extension import fs as grid_fs
from .routes import bp
from .models import User
from config import Config
from gridfs import GridFS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)
    login_manager.init_app(app)

    # Setup GridFS
    global fs
    mongo.fs = GridFS(mongo.db) # type: ignore

    # User loader
    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

    app.register_blueprint(bp)

    return app