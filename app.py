import sqlite3
# flaskからFlaskなどなどをインポート(*を使うと全部インポートできるようになる)
from flask import *
# appという名前でFlaskアプリを作る
app = Flask(__name__)
# secretkeyの設定（sessionを使えるようにする）
app.secret_key = "sunabaco"

@app.route("/top")
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
        return redirect("/top")
    
    else:
        name = request.form.get("name")
        password = request.form.get("password")

        conn = sqlite3.connect("pinkoro.db")
        c = conn.cursor()
        c.execute("insert into users values(null,?,?)",(name,password))
        conn.commit()
        c.close()

        return redirect("/top")



























if __name__ == "__main__":
    app.run(debug=True)