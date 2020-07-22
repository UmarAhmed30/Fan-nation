from flask import Flask,render_template,request,url_for
from flask_cors import CORS

import cx_Oracle

app=Flask(__name__)
CORS(app)

@app.route('/')
def homepage():
    print("NOOOOOB")
    return render_template("./MovieBase/homepage.html")

@app.route('/fan-sign-up',methods=["POST"])
def fan_sign_up():
    fan = request.get_json(force=True)
    print(fan)

    conn = cx_Oracle.connect("Umar/ahmed3633@localhost/orcl")
    cur = conn.cursor()

    sql = """ insert into fan (email_id,name,password) values (:1,:2,:3) """
    cur.execute(sql,[fan['email'],fan['name'],fan['password']])

    conn.commit()
    cur.close()

    return {"status":True}

@app.route('/fan-sign-in',methods=["POST"])
def fan_validation():
    print("SIGNINVHEVK")
    fan = request.get_json(force=True)
    print(fan)

    conn = cx_Oracle.connect("Umar/ahmed3633@localhost/orcl")
    cur = conn.cursor()

    sql = """ select name from fan """
    cur.execute(sql)

    name_list = cur.fetchall()
    print(name_list)

    for i in name_list:
        if i[0] == fan['name']:
            
            print(i[0])

            sql = """ select password from fan where name=:1 """
            cur.execute(sql,{'1':i[0]})

            y = cur.fetchone()
            print(y[0])

            if y[0] == fan['password']:
                print("Password Correct")
                return {"w":0}

            else:
                cur.close()
                return {"w":1}

        else:
            cur.close()
            return {"w":2}

    
@app.route('/to_fanpage')
def to_fanPage():
    return render_template("./MovieBase/fanpage.html")

@app.route('/to_moviepage')
def to_moviepage():
    return render_template("./MovieBase/movie.html")

if __name__ == '__main__':
    app.run(debug=True)