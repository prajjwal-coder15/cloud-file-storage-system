from flask import Blueprint, request, jsonify, send_file, render_template, redirect, url_for, current_app, flash
from flask_login import login_required, login_user, logout_user, current_user
from gridfs import GridFS
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired
from .extension import mongo
from .models import User, role_required
import datetime
import io

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    return render_template("index.html")

# ---------------- REGISTER ----------------
@bp.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            flash("Missing fields")
            return render_template("sign_up.html")

        if mongo.db.users.find_one({"email": email}): # type: ignore
            flash("User already exists")
            return render_template("sign_up.html")

        mongo.db.users.insert_one({ # type: ignore
            "email": email,
            "password": generate_password_hash(password),
            "role": "user"
        })

        flash("User created successfully")
        return redirect(url_for("main.sign_in"))

    return render_template("sign_up.html")


# ---------------- LOGIN ----------------
@bp.route("/sign-in", methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            flash("All fields are required")
            return render_template("sign_in.html")

        user = mongo.db.users.find_one({"email": email}) # type: ignore

        if user and check_password_hash(user["password"], password):
            login_user(User(user))
            return redirect(url_for("main.dashboard"))

        flash("Invalid email or password")

    return render_template("sign_in.html")


#----------------- DASHBOARD ----------------
@bp.route("/dashboard")
@login_required
def dashboard():
    files = mongo.fs.find({ # type: ignore
        "metadata.owner_id": current_user.id
    })

    return render_template("dashboard.html", files=files)


# ---------------- UPLOAD ----------------
@bp.route("/upload", methods=["POST"])
@login_required
def upload():
    file = request.files["file"]

    if file:
        mongo.fs.put( # type: ignore
            file,
            filename=file.filename,
            metadata={"owner_id": current_user.id}
        )

    return redirect(url_for("main.dashboard"))




#----------------- DOWNLOAD ----------------
@bp.route("/download/<file_id>")
@login_required
def download_shared_file(file_id):
    try:
        file = mongo.fs.get(ObjectId(file_id))  # type: ignore
    except Exception:
        flash("File not found")
        return redirect(url_for("main.dashboard"))

    # Optional: ensure user owns the file
    if file.metadata.get("owner_id") != current_user.id:
        flash("Unauthorized access")
        return redirect(url_for("main.dashboard"))

    return send_file(
        io.BytesIO(file.read()),
        download_name=file.filename,
        as_attachment=True
    )

# ---------------- LOGOUT ----------------
@bp.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))