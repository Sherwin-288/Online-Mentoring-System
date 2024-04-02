from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'sherwin@288',
    'database': 'test'
}

@app.route('/hod_login', methods=['POST'])
def hod_login():
    username = request.form['username']
    password = request.form['password']
    department = request.form['department']

    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Execute the query to fetch students based on the selected department
        query = "SELECT * FROM students WHERE department = %s"
        cursor.execute(query, (department,))

        # Fetch all the students
        students = cursor.fetchall()

        # Check if the user exists
        if cursor.fetchone():
            return render_template('students.html', students=students)
        else:
            return 'Login failed: Username or Password is incorrect.'
    except mysql.connector.Error as e:
        return f"Database error: {e}"
    finally:
        # Close the database connection
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)
