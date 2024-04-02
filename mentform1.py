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
        scores = [request.form[f'score{i}'] for i in range(1, 9)]

        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO feedback (score1, score2, score3, score4, score5, score6, score7, score8, roll_no) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                           (scores[0], scores[1], scores[2], scores[3], scores[4], scores[5], scores[6], scores[7], roll_no))
            conn.commit()
            message = "THANKS FOR YOUR FEEDBACK!!"
        except Exception as e:
            conn.rollback()
            message = f"Error: {str(e)}"

        conn.close()
        return message

if __name__ == '__main__':
    app.run(debug=True)
