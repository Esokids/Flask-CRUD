from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)
con = mysql.connector.connect(user='root', password='', host='localhost', database='flask_db')

@app.route('/')
def index():
    cursor = con.cursor()

    query = "SELECT * FROM student"
    cursor.execute(query)
    rows = cursor.fetchall
    cursor.close()
    return render_template('index.html', data=rows)
        
@app.route('/student')
def studentForm():
    return render_template('addStudent.html')

@app.route('/insert', methods=['POST'])
def insert():
    if request.method=="POST":
        fname = request.form['fname']
        lname = request.form['lname']

        cursor = con.cursor()

        query = "INSERT INTO `student` (firstname, lastname) VALUES (%s, %s)"
        cursor.execute(query, (fname, lname))

        con.commit()
        cursor.close()
        return redirect('/')

@app.route('/delete/<id>')
def delete(id):
    cursor = con.cursor()

    query = "DELETE FROM `student` WHERE id={}".format(id)
    cursor.execute(query)

    con.commit()
    cursor.close()
    return redirect('/')

@app.route('/update', methods=['POST'])
def update():
    if request.method=="POST":
        id = request.form['id']
        fname = request.form['fname']
        lname = request.form['lname']

        cursor = con.cursor()

        query = "UPDATE `student` SET firstname=%s, lastname=%s WHERE id=%s"
        cursor.execute(query, (fname, lname, id))

        con.commit()
        cursor.close()
        return redirect('/')
    



if __name__ == "__main__":
    app.run(debug=True)