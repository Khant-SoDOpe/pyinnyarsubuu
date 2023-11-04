from flask import Flask, render_template, request, redirect, url_for, session
import redis
from functools import wraps

app = Flask(__name__)

def require_auth(view):
  @wraps(view)
  def wrapped_view(*args, **kwargs):
    if 'authenticated' in session:
      return view(*args, **kwargs)
    return redirect(url_for('loginpage'))
  return wrapped_view

r = redis.Redis(
  host= "civil-toad-41431.upstash.io",
  port= 41431,
  password= "8014df124c984ed48d6e0bbbc9ea6153"
)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/alive")
def alive():
  return "Alive"





@app.route("/HIC")
@require_auth
def hic():
  return render_template("hear.html")


@app.route("/VIC")
@require_auth
def vic():
  return render_template("visual.html")


#-------------------------------------essential
@app.route("/essential")
def essentialpage():
  return render_template("essential.html")

@app.route("/essential/earH")
@require_auth
def earH():
  return render_template("earHealth.html")

@app.route("/essential/literature")
@require_auth
def essentialliterature():
  return render_template("EssentialLiterature.html")


@app.route("/essential/sexeducation")
@require_auth
def essentialsexeducation():
  return render_template("EssentialSexEducation.html")


# --------------------------------------------steam
@app.route("/steam")
def steam():
  return render_template("steam.html")


@app.route("/steam/Sci")
@require_auth
def steamSci():
  return render_template("steamScience.html")

@app.route("/steam/Sci/PHOSIS")
@require_auth
def PHOSIS():
  return render_template("photosynthesis.html")


#---------------------------------------------formal education

@app.route("/FormalEducation")
def formaleducation():
  return render_template("formalEducationGrade.html")


@app.route("/FormalEducation/Subjects")
def FormalEducationSubjects():
  return render_template("FormalEducation.html")


@app.route("/FormalEducation/Subjects/myanmar")
def myanmar():
  return render_template("myan.html")

@app.route("/FormalEducation/Subjects/myanmar/yaythalpyazat")
@require_auth
def yaythalpyazat():
  return render_template("yaythalpyazat.html")


@app.route("/FormalEducation/Subjects/myanmar/mahawthahtar")
@require_auth
def mahawthahtar():
  return render_template("myanmar.html")


@app.route("/science")
def science():
  return render_template("science.html")

#----------------------------------signup,login
@app.route("/signuppage")
def signuppage():
    return render_template("signup.html")


@app.route("/aboutus")
def aboutus():
    return render_template("about.html")


@app.route("/loginpage")
def loginpage():
    return render_template("login.html")


# ----------------------------------------------------------------------login
@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("Email")
    password = request.form.get("Password")

    # Retrieve user data from Redis
    user_data = r.hgetall(email)

    if user_data:
        if user_data[b'Password'].decode('utf-8') == password:
            # Set the user as authenticated in the session
            session['authenticated'] = True
            letter = 'Successfully Login!'
            return render_template('show.html', contact=letter)
        else:
            letter = 'Please Check Your Password!'
            return render_template('show.html', contact=letter)
    else:
        letter = 'No Account Found!'
        return render_template('show.html', contact=letter)


# ----------------------------------------------------------signup
@app.route("/signup", methods=["POST"])
def signup():
    name = request.form.get("Name")
    email = request.form.get("Email")
    password = request.form.get("Password")
    password2 = request.form.get("Password2")

    if password == password2:
        # Check if the user already exists
        if r.exists(email):
            letter = "Already Have an Account!"
            return render_template('show.html', contact=letter)

        # Store user data in Redis
        user_data = {
            'Name': name,
            'Email': email,
            'Password': password
        }
        r.hmset(email, user_data)
        
        letter = "Successfully Created!"
        return render_template('show.html', contact=letter)
    else:
        letter = "Please Check Your Password!"
        return render_template('show.html', contact=letter)

@app.route("/logout")
@require_auth
def logout():
  session.pop('authenticated', None)  # Remove the 'authenticated' key from the session
  return redirect(url_for('loginpage'))

if __name__ == "__main__":
  app.secret_key = my_secret = "handsomeKhant"
  app.run(host='0.0.0.0', port=5000) 