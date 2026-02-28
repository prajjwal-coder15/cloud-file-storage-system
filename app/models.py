from flask_login import UserMixin, current_user
from bson.objectid import ObjectId
from flask import jsonify
from app.extension import mongo

class User(UserMixin):
    def __init__(self, user_data):
        self.id = str(user_data["_id"])
        self.email = user_data["email"]
        self.role = user_data["role"]

    @staticmethod
    def get(user_id):
        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})  # type: ignore
        return User(user) if user else None


def role_required(role):
    def wrapper(fn):
        def decorated(*args, **kwargs):
            if not current_user.is_authenticated:
                return jsonify({"msg": "Login required"}), 401
            if current_user.role != role:
                return jsonify({"msg": "Forbidden"}), 403
            return fn(*args, **kwargs)
        decorated.__name__ = fn.__name__
        return decorated
    return wrapper