#flask notes: tutoreal
#What does Flask do?
#alows mutipule page websites

#What are the steps to setting up a Flask project?
#

#How can you reference subpages on your Flask project? (Meaning the difference between the home page and a personal profile)
#/name of page

#What are templates?
#alows you to make a website with mutipul html tags
from flask import Flask, render_template, rwquest, rederect, url_for

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request,method == "POST":
        return redirect(url_for("user", name=request.form["name"]))
    return render_template("index.html")

@app.route("/contact")
def contact():
    return "<p>Don't contact me. I don't want to talk to you</p>"

@app.route("/<name>")
def user(name):
    return f"<h1>Hello {name}!</h1>"

if __name__ == "__main__":
    app.run(debug=True)