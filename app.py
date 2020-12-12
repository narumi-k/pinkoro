import sqlite3,datetime
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
    conn = sqlite3.connect("pinkoro.db")
    c = conn.cursor()
    c.execute("select name,comment,image,datetime from bbs")
    comment_list = []
    for row in c.fetchall():
        comment_list.append({"name": row[0], "comment": row[1], "image":row[2], "time":row[3]})
    c.close()
    return render_template('bbs.html' , comment_list = comment_list)


@app.route("/add",methods=["POST"])
def add():
    time = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    name = request.form.get("name")
    comment = request.form.get("comment")

    conn = sqlite3.connect("pinkoro.db")
    c = conn.cursor()
    c.execute("insert into bbs values(null,?,?,?,?)",(name,comment,image,time))
    conn.commit()
    conn.close()

    return redirect("/bbs") 

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
