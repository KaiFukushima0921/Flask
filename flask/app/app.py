from flask import Flask,render_template

# Flaskオブジェクトの作成
app = Flask(__name__)


# 「/」へアクセスがあった場合に、"Hello world"の文字列を返す
@app.route("/")
def hello():
    return "Hello world"


# 「/index」へアクセスがあった場合に、「index.html」を返す
@app.route("/index")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)