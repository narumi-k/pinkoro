import sqlite3,datetime,os
# flaskからFlaskなどなどをインポート(*を使うと全部インポートできるようになる)
from flask import *
# appという名前でFlaskアプリを作る
app = Flask(__name__)
# secretkeyの設定（sessionを使えるようにする）
app.secret_key = "sunabaco"


# トップページ

@app.route("/")
def top():
    return render_template("top.html")

# 投稿ページ（表示）


@app.route("/bbs")
def bbs():

    conn = sqlite3.connect("pinkoro.db")
    c = conn.cursor()

    c.execute("select id,name,comment,image,time from bbs where del_flg = 0")
    comment_list = []
    for row in c.fetchall():
        comment_list.append({"id": row[0], "name": row[1], "comment": row[2], "image": row[3], "time":row[4]})
    
    c.close()

    return render_template('bbs.html', comment_list = comment_list)



# 投稿ページ（投稿）

@app.route("/add",methods=["POST"])
def add():
    time = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    name = request.form.get("name")
    comment = request.form.get("comment")
    upload = request.files['upload']
    unit = request.files['unit']
    upload_string = str(upload)
    unit_string = str(unit)
    print (upload)
    print (unit)

    if upload_string == unit_string:

        conn = sqlite3.connect("pinkoro.db")
        c = conn.cursor()
        c.execute("insert into bbs values(null,?,?,null,?,0)",(name,comment,time))
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
        c.execute("insert into bbs values(null,?,?,?,?,0)",(name,comment,filename,time))
        conn.commit()
        c.close()

        return redirect("/bbs") 

# 返信ページ（表示）

@app.route("/reply/<int:id>",methods=["GET","POST"])
def reply(id):

    if request.method == ["GET"]:

        conn = sqlite3.connect("pinkoro.db")
        c = conn.cursor()
        c.execute("select id,name,comment,image,time from bbs where del_flg = 0 and id = ?",(id,))
        comment_list = []
        for row in c.fetchall():
            comment_list.append({"id": row[0], "name": row[1], "comment": row[2], "image": row[3], "time":row[4]})
        print("-------------------------")
        print(comment_list)

        c.execute("select reply_id,reply_name,reply_comment,reply_time from reply join bbs on bbs.id = reply.comment_id where reply_del_flg = 0 and bbs.id = ?",(id,))
        reply_list = []
        for row in c.fetchall():
            reply_list.append({"id": row[0], "name": row[1], "comment": row[2], "time":row[3]})
        print("-------------------------")
        print(reply_list)

        c.execute("select id from bbs where id = ?",(id,))
        comment_id = c.fetchone()[0]
        print(comment_id)

        c.close()

        return render_template("reply.html", comment_list = comment_list, reply_list = reply_list, comment_id = comment_id)

    else:

        comment_id = request.form.get("comment_id")
        time = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        name = request.form.get("reply_name")
        comment = request.form.get("reply_comment")

        conn = sqlite3.connect("pinkoro.db")
        c = conn.cursor()
        c.execute("insert into reply values(null,?,?,?,?,0)",(comment_id,name,comment,time))

        c.execute("select id,name,comment,image,time from bbs where del_flg = 0 and id = ?",(id,))
        comment_list = []
        for row in c.fetchall():
            comment_list.append({"id": row[0], "name": row[1], "comment": row[2], "image": row[3], "time":row[4]})
        print("-------------------------")
        print(comment_list)

        c.execute("select reply_id,reply_name,reply_comment,reply_time from reply join bbs on bbs.id = reply.comment_id where reply_del_flg = 0 and bbs.id = ?",(id,))
        reply_list = []
        for row in c.fetchall():
            reply_list.append({"id": row[0], "name": row[1], "comment": row[2], "time":row[3]})
        print("-------------------------")
        print(reply_list)

        c.execute("select id from bbs where id = ?",(id,))
        comment_id = c.fetchone()[0]
        print(comment_id)

        conn.commit()
        c.close()

        return render_template("reply.html", comment_list = comment_list, reply_list = reply_list, comment_id = comment_id)


# 返信ページ（投稿）







@app.route("/course")
def course():
    return render_template("course.html")

@app.route("/intro")
def intro():
    return render_template("intro.html")

<<<<<<< HEAD
@app.route("/del/<int:id>")
def del_comment(id):

    conn = sqlite3.connect("pinkoro.db")
    c = conn.cursor()
    c.execute("update bbs set del_flg = 1 where id =?",(id,))
    conn.commit()
    c.close()

    return redirect("/bbs")
=======
@app.route("/taiyou")
def taiyou():
    return render_template("taiyou.html")

@app.route("/mugishima")
def mugishima():
    return render_template("mugishima.html")

@app.route("/sakamoto")
def sakamoto():
    return render_template("sakamoto.html")

@app.route("/miyaji")
def miyaji():
    return render_template("miyaji.html")

>>>>>>> 46663daffb9739aeca709e32253fe00148f70b82








@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"),404




if __name__ == "__main__":
    app.run(debug=True)
