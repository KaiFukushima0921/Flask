from flask import Flask,render_template,request
from .models.models import OnegaiContent

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    show_name = request.args.get("a")
    all_onegai = OnegaiContent.query.all()
    return render_template("index.html", name = show_name, all_onegai = all_onegai)


@app.route("/index", methods=["post"])
def post():
    name = request.form["name2"]
    all_onegai = OnegaiContent.query.all()
    return render_template("index.html", name = name, all_onegai = all_onegai)


if __name__ == "__main__":
    app.run(debug=True)