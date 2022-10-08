from flask import Flask, request, jsonify
import mysql.connector as conn
app = Flask(__name__)



@app.route("/testfun")
def test():
    get_name = request.args.get("get_name")
    mobile_number = request.args.get("mobile")
    mail_id = request.args.get("mail_id")
    return 'This is my first get function {} {} {}'.format(get_name,mobile_number,mail_id)


@app.route("/mydb")
def access_db():
    get_db = request.args.get("get_db")
    get_tbl = request.args.get("get_tbl")
    mydb = conn.connect(host="localhost", user="root", password="root", port="3308")
    cursor = mydb.cursor()
    print(get_tbl,get_db,type(get_tbl))
    cursor.execute("select * from %s . %s",get_db,get_tbl)
    l = []
    for i in cursor.fetchall():
        l.append(i)
        print(l)
    return jsonify(str(l))

if __name__=="__main__":
    app.run()
