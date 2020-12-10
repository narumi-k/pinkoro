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

@app.route("/taiyou")
def taiyou():
    return render_template("taiyou.html")

@app.route("/ootago")
def ootago():
    return render_template("ootago.html")

@app.route("/kongou")
def kongou():
    return render_template("kongou.html")

@app.route("/matsutaka")
def matsutaka():
    return render_template("matsutaka.html")

@app.route("/regist",methods=["GET"])
def regist_get():
    if "user_id" in session:
        return render_template("/top")
    else:
        return render_template("regist.html")

@app.route("/regist",methods=["POST"])
def regist_post():
    if "user_id" in session:
        return redirect("/")
    
    else:
        name = request.form.get("name")
        password = request.form.get("password")

        conn = sqlite3.connect("pinkoro.db")
        c = conn.cursor()
        c.execute("insert into users values(null,?,?)",(name,password))
        conn.commit()
        c.close()

        return redirect("/")

@app.route("/",methods=["POST"])
def login_post():
    name = request.form.get("name")
    password = request.form.get("password")

    conn = sqlite3.connect("pinkoro.db")
    c = conn.cursor()
    c.execute("select id from users where name = ? and password = ?",(name,password))
    user_id = c.fetchone()
    c.close()

    if user_id is None:
        return render_template("regist.html")
    else:
        session["user_id"] = user_id[0]
        return redirect("/")




















@app.route("/logout")
def logout():
    session.pop("user_id",None)
    return redirect("/")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"),404



if __name__ == "__main__":
    app.run(debug=True)