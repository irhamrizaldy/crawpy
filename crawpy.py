from flask import Flask
from flask import render_template
from flask import request #This imports the request module from Flask, which allows us to easily handle many aspects of HTTP requests, including data sent via forms.

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        print(request.form)
    # return "My Flask app"
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host='localhost', debug=True)