from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="oms"
)

cursor = db.cursor()


@app.route('/')
def index():
    return render_template('adminlogin.html')


@app.route('/', methods=['GET', 'POST'])
def admin_connect():
    if request.method == 'POST':
        uname = request.form['uname']
        pwd = request.form['pass']

        try:
            cursor.execute("SELECT * FROM admin WHERE uname = %s AND pass = %s", (uname, pwd))
            result = cursor.fetchone()
            if result:
                return redirect(url_for('admin_select'))
            else:
                return 'Login failed!'
        except mysql.connector.Error as e:
            return f"Database error: {e}"
    else:
        return render_template('adminlogin.html')


@app.route('/adminselect', methods=['GET', 'POST'])
def admin_select():
    if request.method == 'GET':
        try:
            # Fetch departments
            cursor.execute("SELECT dept_id, dept_name FROM department")
            departments = cursor.fetchall()

            # Fetch semesters
            cursor.execute("SELECT seme FROM semester")
            semesters = cursor.fetchall()

            # Render admin selection page with fetched data
            return render_template('adminselect.html', departments=departments, semesters=semesters)
        except mysql.connector.Error as e:
            return f"Database error: {e}"
    elif request.method == 'POST':
        # Handle form submission here
        # Extract selected department, semester, division from request.form and perform further actions
        pass  # Placeholder for further processing


if __name__ == '__main__':
    app.run(debug=True)
