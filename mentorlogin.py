from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Configure MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sherwin@288",
    database="test"
)

cursor = db.cursor()

@app.route('/')
def mentor_login_form():
    return render_template('mentorlogin.html')

@app.route('/login', methods=['POST'])
def mentor_login():
    username = request.form['mentid']
    password = request.form['pass']

    query = "SELECT * FROM mentor_table WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    mentor = cursor.fetchone()

    if mentor:
        mentor_id = mentor[0]
        mentor_dept = mentor[1]
        return f"Mentor LOGGED IN SUCCESSFULLY! Mentor ID: {mentor_id}, Department: {mentor_dept}"

    else:
        return "LOGIN FAILED: Username or password is incorrect."

if __name__ == '__main__':
    app.run(debug=True)
