from flask import Flask,render_template,redirect,url_for,flash,request
import sqlite3 as sql
app=Flask(__name__)

app.secret_key= "your_secret_key"

@app.route('/')
@app.route('/index')
def index():
    conn=sql.connect("db_web.db")
    conn.row_factory=sql.Row
    cursor=conn.cursor()
    cursor.execute('select * from users')
    data=cursor.fetchall()
    return render_template('index.html',datas=data)

@app.route('/add_user',methods=['POST','GET'])
def add_user():
    if request.method =='POST':
        uname=request.form['uname']
        contact=request.form['contact']
        conn=sql.connect('db_web.db')
        cursor=conn.cursor()
        cursor.execute('insert into users (uname,contact) values(?,?)',(uname,contact))
        conn.commit()
        flash('user added','success')
        return redirect('/index')
    return render_template('add_user.html')

@app.route('/edit_user/<string:uid>',methods=['POST','GET'])
def edit_user(uid):
    if request.method=='POST':
        uname=request.form['uname']
        contact=request.form['contact']
        conn=sql.connect('db_web.db')
        cursor=conn.cursor()
        cursor.execute('update users set uname=?,contact=? where UID=?',(uname,contact,uid))
        conn.commit()
        flash('user updated','success')
        return redirect(url_for('index'))
    conn=sql.connect('db_web.db')
    conn.row_factory=sql.Row
    cursor=conn.cursor()
    cursor.execute('select * from users where UID=?',(uid,))
    data=cursor.fetchone()
    return render_template('edit_user.html',datas=data)

@app.route('/delete_user/<string:uid>',methods=['GET'])
def delete_user(uid):
    conn=sql.connect('db_web.db')
    cursor=conn.cursor()
    cursor.execute('delete from users where UID=?',(uid,))
    conn.commit()
    flash('user deleted','warning')
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)