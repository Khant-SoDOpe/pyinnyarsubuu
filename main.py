from flask import Flask, render_template, request
from random import randint
import csv

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/PHOSIS")
def PHOSIS():
    return render_template("photosynthesis.html")


@app.route("/HIC")
def hic():
    return render_template("hear.html")


@app.route("/VIC")
def vic():
    return render_template("visual.html")


#-------------------------------------essential
@app.route("/essential")
def essentialpage():
    return render_template("essential.html")

@app.route("/essential/earH")
def earH():
    return render_template("earHealth.html")

@app.route("/essential/literature")
def essentialliterature():
    return render_template("EssentialLiterature.html")


@app.route("/essential/sexeducation")
def essentialsexeducation():
    return render_template("EssentialSexEducation.html")


# --------------------------------------------steam
@app.route("/steam")
def steam():
    return render_template("steam.html")


@app.route("/steam/Sci")
def steamSci():
    return render_template("steamScience.html")


@app.route("/steam/PST")
def steamPST():
    return render_template("photosynthesis.html")


#---------------------------------------------formal education
@app.route("/yaythalpyazat")
def yaythalpyazat():
    return render_template("yaythalpyazat.html")


@app.route("/mahawthahtar")
def mahawthahtar():
    return render_template("myanmar.html")


@app.route("/science")
def science():
    return render_template("science.html")


@app.route("/myanmar")
def myanmar():
    return render_template("myan.html")


@app.route("/FormalEducation")
def formaleducation():
    return render_template("formalEducationGrade.html")


@app.route("/FormalEducation/Subjects")
def FormalEducationSubjects():
    return render_template("FormalEducation.html")


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
    print(email, password)

    with open("data.csv", "r") as data_file:
        all_data = csv.DictReader(data_file)

        for emails in all_data:
            if emails['Email'] == email:
                if emails['Password'] == password:
                    letter = 'Sucessfully Login!'
                    return render_template('show.html', contact=letter)
                else:
                    letter = 'Pls Check Your Password!'
                    return render_template('show.html', contact=letter)

        letter = 'No Account Found!'
        return render_template('show.html', contact=letter)


@app.route("/signup", methods=["POST"])
def signup():
    def add(email, password, name):
        user_data = {}

        user_data["Name"] = name
        user_data["Email"] = email
        user_data["Password"] = password

        print(user_data)

        fieldnames = []
        for key in user_data:
            fieldnames.append(key)

        with open("data.csv", "a") as data_file:
            writer = csv.DictWriter(data_file, fieldnames)
            writer.writerow(user_data)

    name = request.form.get("Name")
    email = request.form.get("Email")
    password = request.form.get("Password")
    password2 = request.form.get("Password2")
    permission = 'allowed'
    if password == password2:
        with open('data.csv', "r") as append_file:
            data = csv.DictReader(append_file)

            for emails in data:
                print(emails)
                if emails['Email'] == email:
                    permission = 'disallowed'

            if permission == 'allowed':
                add(email, password, name)
                print('reach sucess')
                letter = "Sucessfully created!"
                return render_template('show.html', contact=letter)
            else:
                letter = "Already Have a account!"
                return render_template('show.html', contact=letter)
    else:
        letter = "Pls check your password!"
        return render_template('show.html', contact=letter)


# ----------------------------------------------------------signup

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=randint(2000, 9000))