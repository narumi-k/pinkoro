import sqlite3,datetime,os
from werkzeug.utils import secure_filename
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
    c.execute("select name,comment,image,time from bbs")
    comment_list = []
    for row in c.fetchall():
        comment_list.append({"name": row[0], "comment": row[1], "image": row[2], "time":row[3]})
    c.close()
    return render_template('bbs.html' , comment_list = comment_list)


@app.route("/add",methods=["POST"])
def add():
    time = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    name = request.form.get("name")
    comment = request.form.get("comment")
    upload = request.files['upload']
    unit = request.files['unit']
    upload_string =str(upload)
    unit_string = str(unit)
    print (upload)
    print (unit)

    if unit_string == upload_string:
        print('igg')
        conn = sqlite3.connect("pinkoro.db")
        c = conn.cursor()
        c.execute("insert into bbs values(null,?,?,null,?)",(name,comment,time))
        conn.commit()
        conn.close()

        return redirect("/bbs")
    
    else:

        def get_save_path():
            path_dir = "./static/upload"
            return path_dir

        upload.filename.lower()

        # 下の def get_save_path()関数を使用して "./static/upload/" パスを戻り値として取得する。
        save_path = get_save_path()
        print(save_path)
        # ファイルネームをfilename変数に代入(file名だけを変数に入れる)
        filename = upload.filename
        # 画像ファイルを./static/uploadフォルダに保存。
        # os.path.join()は、パスとファイル名をつないで返してくれます。
        upload.save(os.path.join(save_path,filename))
        # ファイル名が取れることを確認、あとで使うよ
        print(filename)

        conn = sqlite3.connect("pinkoro.db")
        c = conn.cursor()
        c.execute("insert into bbs values(null,?,?,?,?)",(name,comment,filename,time))
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
