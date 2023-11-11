from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    show_name = request.args.get("a")
    okyo = ["色不異空","空不異色","色即是空","空即是色"]
    return render_template("index.html",name=show_name,ok=okyo)


@app.route("/index", methods=["post"])
def post():
    name = request.form["name2"]
    okyo = ["色不異空", "空不異色", "色即是空", "空即是色"]
    return render_template("index.html", name = name, okyo = okyo)


if __name__ == "__main__":
    app.run(debug=True)