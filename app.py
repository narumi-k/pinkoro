import sqlite3
# flaskからFlaskなどなどをインポート(*を使うと全部インポートできるようになる)
from flask import *
# appという名前でFlaskアプリを作る
app = Flask(__name__)
# secretkeyの設定（sessionを使えるようにする）
app.secret_key = "sunabaco"


@app.route("/")
def top():
    return render_template("top.html")


@app.route("/bbs")
def bbs():
    return render_template("bbs.html")

@app.route("/course")
def course():
    return render_template("course.html")

@app.route("/intro")
def intro():
    return render_template("intro.html")







@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"),404




if __name__ == "__main__":
    app.run(debug=True)
