from flask import Flask, render_template, request
import mysql.connector
from flask import jsonify

app = Flask(__name__)

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sherwin@288",  # Replace with your MySQL password
    database="test"
)

cursor = db.cursor()

# Options for branch, division, and semester
branch_options = ['IT', 'Comps', 'Mech', 'Elect', 'EXTC']
division_options = {'Comps': ['A', 'B'], 'Mech': ['A', 'B']}
semester_options = ['1', '2', '3', '4', '5', '6', '7', '8']


@app.route('/')
def index():
    return render_template('adminselect.html', branch_options=branch_options)


@app.route('/submit', methods=['POST'])
def submit():
    selected_branch = request.form['branch']
    selected_division = request.form.get('division')
    selected_semester = request.form['semester']

    # Here you can perform database operations
    # For now, let's just print the selected options
    print(f"Selected Branch: {selected_branch}")
    print(f"Selected Division: {selected_division}")
    print(f"Selected Semester: {selected_semester}")

    return "Selection submitted successfully!"


@app.route('/division_options', methods=['POST'])
def get_division_options():
    branch = request.form['branch']
    divisions = division_options.get(branch, [])
    return jsonify({'divisions': divisions})


if __name__ == '__main__':
    app.run(debug=True)
