from flask import *
from flask_mail import *
from flask_login import login_required
from random import *
import sqlite3

app=Flask(__name__)

# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'minhajul.islam0509@gmail.com'
app.config['MAIL_PASSWORD'] = 'NHPython06'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)
otp=randint(000000,999999)

@app.route('/')
def layout():
    return render_template('layout.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/reg',methods=["POST","GET"])
def reg():
    email = request.form['email']
    msg = Message(subject="Email Verification", sender="minhajul.islam0509@gmail.com",
                  recipients=[email])
    msg.body = str(otp)
    mail.send(msg)
    return render_template("OtpCheck.html")

@app.route('/CheckOtp',methods=['POST'])
def validitycheck():
    msg = None
    userOtp=request.form['check']
    if otp == int(userOtp) and request.form["key"]=='Admin knows':
        username=request.form["name"]
        email=request.form['email']
        password=request.form["pass"]
        con=sqlite3.connect('admin.db')
        cur=con.cursor()
        cur.execute("INSERT INTO admins(Username,Email,Password) VALUES(?,?,?)",(username,email,password))
        con.commit()
        msg="You are registered now!"
        return render_template("OtpCheck.html",**locals())
    msg="Something went wrong!"
    return render_template('OtpCheck.html',**locals())

@login_required
@app.route('/login')
def login():
        return render_template('login.html')
@app.route('/log',methods=["POST","GET"])
def log():
    msg=None
    if request.method=="POST":
        # username=request.form["name"]
        email=request.form["email"]
        password=request.form["pass"]
        con=sqlite3.connect('admin.db')
        cur=con.cursor()
        find_user=("SELECT* FROM admins WHERE Email=? AND Password=?")
        cur.execute(find_user,[(email),(password)])
        results=cur.fetchall()

        if results:
            for i in results:
                return render_template("home.html")
        else:
            msg = "Invalid Username or Password!"
            return render_template('login.html',**locals())
@app.route('/studentregistration')
def studentregistration():
    return render_template('studentregistration.html')
@app.route('/sreg',methods=["POST","GET"])
def sreg():
    email = request.form['email']
    msg = Message(subject="Email Verification", sender="minhajul.islam0509@gmail.com",
                  recipients=[email])
    msg.body = str(otp)
    mail.send(msg)
    return render_template("SOtpCheck.html")

@app.route('/CheckSOtp',methods=['POST'])
def svaliditycheck():
    msg=None
    userOtp=request.form['check']
    if otp == int(userOtp):
        username=request.form["name"]
        email=request.form['email']
        password=request.form["pass"]
        con=sqlite3.connect('student.db')
        cur=con.cursor()
        cur.execute("INSERT INTO students(Username,Email,Password) VALUES(?,?,?)",(username,email,password))
        con.commit()
        msg="You are registered now!"
        return render_template("SOtpCheck.html",**locals())
    msg="Something went wrong!"
    return render_template("SOtpCheck.html",**locals())

@login_required
@app.route('/studentlogin')
def studentlogin():
    return render_template('studentlogin.html')
@app.route('/slog',methods=["POST","GET"])
def slog():
    msg=None
    if request.method=="POST":
        # username=request.form["name"]
        email=request.form["email"]
        password=request.form["pass"]
        con=sqlite3.connect('student.db')
        cur=con.cursor()
        find_user=("SELECT* FROM students WHERE Email=? AND Password=?")
        cur.execute(find_user,[(email),(password)])
        results=cur.fetchall()

        if results:
            for i in results:
                return render_template("shome.html")
        else:
            msg = "Invalid Username or Password!"
            return render_template("studentlogin.html",**locals())


@app.route('/shome')
def shome():
    return render_template('shome.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/insert')
def insert():
    return render_template('Insert.html')
@app.route('/in',methods=["POST","GET"])
def ins():
    msg=None
    if request.method=="POST":
        name=request.form["name"]
        reg=request.form["reg"]
        first=request.form['first']
        second=request.form['second']
        third=request.form['third']
        fourth=request.form['fourth']
        fifth=request.form['fifth']
        sixth=request.form['sixth']
        seventh=request.form['seventh']
        eight=request.form['eight']
        con=sqlite3.connect('dt.db')
        cur=con.cursor()
        cur.execute("INSERT INTO data(name,studentID,firstSem,secondSem,thirdSem,fourthSem,fifthSem,sixthSem,seventhSem,eightSem) VALUES(?,?,?,?,?,?,?,?,?,?)",(name,reg,first,second,third,fourth,fifth,sixth,seventh,eight))
        con.commit()
        msg="Successfully Added"
        return render_template('insert.html',**locals())


@app.route('/view', methods=["GET"])
def view():
    con=sqlite3.connect('dt.db')
    con.row_factory=sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT* FROM data")
    rows=cur.fetchall()
    return render_template('view.html',rows=rows)


@app.route('/update')
def update():
    return render_template('update.html')
@app.route('/up', methods=["POST","GET"])
def up():
    msg=None
    if request.method=="POST":
        name = request.form["name"]
        reg = request.form["reg"]
        first = request.form['first']
        second = request.form['second']
        third = request.form['third']
        fourth = request.form ['fourth']
        fifth = request.form['fifth']
        sixth = request.form['sixth']
        seventh = request.form['seventh']
        eight = request.form['eight']
        con = sqlite3.connect('dt.db')
        cur = con.cursor()
        cur.execute("UPDATE data SET name=?,firstSem=?,secondSem=?,thirdSem=?,fourthSem=?,fifthSem=?,sixthSem=?,seventhSem=?,eightSem=? WHERE studentID=?",(name,first,second,third,fourth,fifth,sixth,seventh,eight,reg))
        con.commit()
        msg="Successfully updated!"
        return render_template('update.html',**locals())
@app.route('/delete')
def delete():
    return render_template('delete.html')
@app.route('/delet', methods=["POST"])
def delet():
    msg=None
    if request.method=="POST":
        reg=request.form["reg"]
        con=sqlite3.connect('dt.db')
        cur=con.cursor()
        cur.execute("DELETE FROM data WHERE studentID=?",[reg])
        con.commit()
        msg="Successfully deleted!"
        return render_template("delete.html",**locals())


if __name__=='__main__':
    app.run(debug=True)