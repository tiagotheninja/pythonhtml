from flask import Flask, render_template, request, make_response
import random

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    response = make_response(render_template("index.html"))
    if not request.cookies.get("secret"):
        response.set_cookie("secret", str(random.randint(1,30)))

    return response


@app.route("/submit", methods=["POST"])
def submit():
    cookie_secret = int(request.cookies.get("secret"))
    try_secret = int(request.form.get("guess"))

    if cookie_secret == try_secret:
        message = "congratz!"
        response = make_response(render_template("submit.html", message=message))
        response.set_cookie("secret", str(random.randint(1,30)))
        return response
    else:
        message = "you fail!"
        return render_template("submit.html", message=message)


if __name__ == "__main__":
    app.run(use_reloader=True)
