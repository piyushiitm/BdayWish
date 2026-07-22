from flask import Flask,render_template,session,request,redirect

app = Flask(__name__)
app.secret_key = "192317"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login",  methods=["POST"])
def login():
    password = request.form["password"].lower()
    if(password=="seeti"):
        session["logged_in"] = True
        return redirect("/Message")
    
    return render_template(
        "home.html",
        error="Bhool Gyi 😒!"
    )

@app.route("/Message")
def message():
    return render_template("message.html")

@app.route("/20thBirthday")
def lastbday():
    return render_template("LastBday.html")

@app.route("/Memories")
def mem():
    return render_template("Memories.html")

@app.route("/BdayCelebration")
def celeb():
    return render_template("Celebration.html")
if __name__ == "__main__":
    app.run(debug=True)