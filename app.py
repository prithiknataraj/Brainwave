from flask import Flask, render_template, request, redirect, session, url_for
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "16dc6a592ff077a7598c710f84fce03edd1c87e794a9955429b7cf4c0ef57970"

cred = credentials.Certificate(r"C:\Users\prith\OneDrive\Desktop\Brainwave\brainwave-ae94f-firebase-adminsdk-agjmo-7c15b3260c.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def calculate_age(dob_str):
    dob = datetime.strptime(dob_str, "%Y-%m-%d")
    today = datetime.today()
    age = today.year - dob.year
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1
    return age

videos_dict = {
    "english": [
        "https://www.youtube.com/embed/wuxu6Qsaq5I?si=4VwJQVAv8qkFBl8h",
        "https://www.youtube.com/embed/NDMPwZL47JY?list=PLZS3MUjYqjUFIVihLicWijrEh5RokMm8J0",
        "https://www.youtube.com/embed/dBm9B2SLEp4?list=PLZS3MUjYqjUFIVihLicWijrEh5RokMm8J0",
        "https://www.youtube.com/embed/UUADD6J07cU?si=ky4O5ckfoIzFMqkH"
    ],
    "maths": [
        "https://www.youtube.com/embed/wuxu6Qsaq5I?si=4VwJQVAv8qkFBl8h",
        "https://www.youtube.com/embed/NDMPwZL47JY?list=PLZS3MUjYqjUFIVihLicWijrEh5RokMm8J0",
        "https://www.youtube.com/embed/dBm9B2SLEp4?list=PLZS3MUjYqjUFIVihLicWijrEh5RokMm8J0",
        "https://www.youtube.com/embed/UUADD6J07cU?si=ky4O5ckfoIzFMqkH"
    ],
    "physics": [
        "https://www.youtube.com/embed/wuxu6Qsaq5I?si=4VwJQVAv8qkFBl8h",
        "https://www.youtube.com/embed/NDMPwZL47JY?list=PLZS3MUjYqjUFIVihLicWijrEh5RokMm8J0",
        "https://www.youtube.com/embed/dBm9B2SLEp4?list=PLZS3MUjYqjUFIVihLicWijrEh5RokMm8J0",
        "https://www.youtube.com/embed/UUADD6J07cU?si=ky4O5ckfoIzFMqkH"
    ],
    "chemistry": [
        "https://www.youtube.com/embed/wuxu6Qsaq5I?si=4VwJQVAv8qkFBl8h",
        "https://www.youtube.com/embed/NDMPwZL47JY?list=PLZS3MUjYqjUFIVihLicWijrEh5RokMm8J0",
        "https://www.youtube.com/embed/dBm9B2SLEp4?list=PLZS3MUjYqjUFIVihLicWijrEh5RokMm8J0",
        "https://www.youtube.com/embed/UUADD6J07cU?si=ky4O5ckfoIzFMqkH"
    ]
}

def Video(age, subject):
    return videos_dict.get(subject, [])

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        existing_user = db.collection('users').where('email', '==', email).get()
        if existing_user:
            return render_template("signup.html", error_message="Email id already registered")
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        if password != confirm_password:
            return render_template("signup.html", error_message="Password does not match")
        gender = request.form.get('gender')
        dob = request.form.get('dob')
        hashed_password = generate_password_hash(password)
        data = {"name": name, "email": email, "password": hashed_password, "gender": gender, "dob": dob}
        session['user_id'] = email
        session['age'] = calculate_age(dob)
        db.collection('users').document().set(data)
        return redirect(url_for('home'))
    else:
        return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        existing_user = db.collection('users').where('email', '==', email).get()
        if existing_user:
            user_data = existing_user[0].to_dict()
            if check_password_hash(user_data['password'], password):
                session['user_id'] = email
                session['age'] = calculate_age(user_data['dob'])
                return redirect(url_for('home'))
        return render_template('login.html', error_message='Invalid email or password')
    else:
        return render_template("login.html")

@app.route("/home", methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route("/course", methods=["GET", "POST"])
def course():
    subject = request.args.get("subject")
    videos = Video(session['age'], subject)
    return render_template("course.html", videos=videos)

@app.route("/meeting", methods=["GET"])
def meeting():
    roomID = request.args.get("roomID")
    return render_template("meeting.html", roomID=roomID)

@app.route("/meet", methods=["GET", "POST"])
def meet():
    return render_template("meet.html")

@app.route("/existing_meeting", methods=["GET", "POST"])
def existing_meeting():
    if request.method == "POST":
        meeting_id = request.form.get("meeting_id")
        return redirect(url_for('meeting', roomID=meeting_id))
    return render_template("existing_meeting.html")

@app.route("/test", methods=["GET", "POST"])
def test():
    return render_template("test.html")

@app.route("/profile", methods=["GET", "POST"])
def profile():
    return render_template("profile.html")

@app.route("/class", methods=["GET", "POST"])
def classes():
    return render_template("class.html")

if __name__ == "__main__":
    app.run(debug=True)
