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
        sports = request.form['sports']
        nsssocialcell = request.form['nsssocialcell']
        comp = request.form['comp']

        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO extra (seme, sports, nsssocialcell, comp, roll_no) VALUES (%s, %s, %s, %s, %s)",
                           (semester, sports, nsssocialcell, comp, roll_no))
            conn.commit()
            message = "You've successfully filled all the forms!!"
        except Exception as e:
            conn.rollback()
            message = f"Error: {str(e)}"

        conn.close()
        return message

if __name__ == '__main__':
    app.run(debug=True)
