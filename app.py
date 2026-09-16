from flask import Flask, render_template, request, redirect, session
from pymongo import MongoClient
from flask_bcrypt import Bcrypt

app = Flask(__name__)

# =========================
# SECRET KEY
# =========================
app.secret_key = "your-random-secret-key-here"

bcrypt = Bcrypt(app)

# =========================
# MONGODB CONNECTION
# =========================
client = MongoClient("MongoDB URL")

db = client["fraudshield"]

reports_collection = db["reports"]
users_collection = db["users"]

print("CONNECTED TO MONGODB")

# =========================
# GLOBAL USER SESSION
# =========================
@app.context_processor
def inject_user():

    return {
        "user": session.get("user"),
        "email": session.get("email")
    }

# =========================
# HOME PAGE
# =========================
@app.route("/")
def home():

    recent_reports = list(
        reports_collection.find().sort("_id", -1).limit(6)
    )

    total_reports = reports_collection.count_documents({})

    total_users = users_collection.count_documents({})

    return render_template(
        "index.html",
        recent_reports=recent_reports,
        total_reports=total_reports,
        total_users=total_users
    )

# =========================
# SIGNUP
# =========================
@app.route("/signup", methods=["GET", "POST"])
def signup():

    message = ""

    if request.method == "POST":

        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        avatar_url = request.form.get("avatar_url")

        print("FORM DATA RECEIVED")
        print("USERNAME:", username)
        print("EMAIL:", email)

        existing_user = users_collection.find_one({
            "email": email
        })

        if existing_user:

            message = "Email already exists"

            print("EMAIL ALREADY EXISTS")

        else:

            hashed_password = bcrypt.generate_password_hash(
                password
            ).decode("utf-8")

            users_collection.insert_one({
                "username": username,
                "email": email,
                "password": hashed_password,
                "avatar_url": avatar_url
            })

            print("USER INSERTED SUCCESSFULLY")

            inserted_user = users_collection.find_one({
                "email": email
            })

            print("DATABASE CHECK:")
            print(inserted_user)

            return redirect("/login")

    return render_template(
        "signup.html",
        message=message
    )

# =========================
# LOGIN
# =========================
@app.route("/login", methods=["GET", "POST"])
def login():

    message = ""

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        user = users_collection.find_one({
            "email": email
        })

        if user and bcrypt.check_password_hash(
            user["password"],
            password
        ):

            session["user"] = user["username"]
            session["email"] = user["email"]

            print("LOGIN SUCCESS")

            return redirect("/")

        else:

            message = "Invalid Email or Password"

            print("LOGIN FAILED")

    return render_template(
        "login.html",
        message=message
    )

# =========================
# LOGOUT
# =========================
@app.route("/logout")
def logout():

    session.clear()

    print("USER LOGGED OUT")

    return redirect("/")

# =========================
# REPORT PAGE
# =========================
@app.route("/report", methods=["GET", "POST"])
def report():

    if "user" not in session:
        return redirect("/login")

    success = ""
    error = ""

    if request.method == "POST":

        phone = request.form.get("phone")
        category = request.form.get("category")
        description = request.form.get("description")

        # ✅ FIXED LOGIC HERE
        existing_report = reports_collection.find_one({
            "phone": phone,
            "category": category,
            "reported_by": session["email"]
        })

        if existing_report:

            error = "You already reported this category for this number."
            print("DUPLICATE CATEGORY REPORT BLOCKED")

        else:

            reports_collection.insert_one({
                "phone": phone,
                "category": category,
                "description": description,
                "reported_by": session["email"]
            })

            success = "Report submitted successfully."
            print("REPORT INSERTED SUCCESSFULLY")

    return render_template(
        "report.html",
        success=success,
        error=error
    )

# =========================
# SEARCH REPORTS
# =========================
@app.route("/reports")
def reports():

    search_query = request.args.get("search")

    result = None
    all_reports = []

    if search_query:

        all_reports = list(
            reports_collection.find({
                "phone": search_query
            }).sort("_id", -1)
        )

        otp = reports_collection.count_documents({
            "phone": search_query,
            "category": "OTP Scam"
        })

        prize = reports_collection.count_documents({
            "phone": search_query,
            "category": "Prize Scam"
        })

        investment = reports_collection.count_documents({
            "phone": search_query,
            "category": "Investment Scam"
        })

        job = reports_collection.count_documents({
            "phone": search_query,
            "category": "Job Scam"
        })

        total = otp + prize + investment + job

        if total >= 6:

            risk = "HIGH RISK"

        elif total >= 3:

            risk = "MODERATE RISK"

        elif total > 0:

            risk = "LOW RISK"

        else:

            risk = "NO REPORTS"

        result = {
            "phone": search_query,
            "otp": otp,
            "prize": prize,
            "investment": investment,
            "job": job,
            "total": total,
            "risk": risk
        }

    return render_template(
        "search.html",
        result=result,
        reports=all_reports
    )

# =========================
# ANALYTICS
# =========================
@app.route("/analytics")
def analytics():

    total = reports_collection.count_documents({})

    otp = reports_collection.count_documents({
        "category": "OTP Scam"
    })

    prize = reports_collection.count_documents({
        "category": "Prize Scam"
    })

    investment = reports_collection.count_documents({
        "category": "Investment Scam"
    })

    job = reports_collection.count_documents({
        "category": "Job Scam"
    })

    recent_reports = list(
        reports_collection.find().sort("_id", -1).limit(100)
    )

    return render_template(
        "analytics.html",
        total=total,
        otp=otp,
        prize=prize,
        investment=investment,
        job=job,
        recent_reports=recent_reports
    )

# =========================
# RUN APP
# =========================
if __name__ == "__main__":

    print("FLASK SERVER STARTED")

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
