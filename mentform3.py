from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'sherwin@288'
DB_NAME = 'test'

# Function to establish MySQL connection
def get_db_connection():
    return mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)

# Index route
@app.route('/')
def index():
    return render_template('index.html')

# Form submission route
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        roll_no = request.form['roll_no']
        semester = request.form['seme']
        perform = request.form['perform']
        internship = request.form['internship']
        published = request.form['published']

        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO place (seme, perform, internship, published, roll_no) VALUES (%s, %s, %s, %s, %s)",
                           (semester, perform, internship, published, roll_no))
            conn.commit()
            message = "Thank you for filling the form!!"
        except Exception as e:
            conn.rollback()
            message = f"Error: {str(e)}"

        conn.close()
        return message

if __name__ == '__main__':
    app.run(debug=True)
