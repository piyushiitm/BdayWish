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

if __name__ == "__main__":
    app.run(debug=True)