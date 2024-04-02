from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/admin_login', methods=['POST'])
def admin_login():
    # Handle admin login
    return render_template('adminlogin.html')


@app.route('/hod_login', methods=['POST'])
def hod_login():
    # Handle HOD login
    return render_template('hodlogin.html')


@app.route('/mentor_login', methods=['POST'])
def mentor_login():
    # Handle mentor login
    return render_template('mentorlogin.html')


@app.route('/student_login', methods=['POST'])
def student_login():
    # Handle student login
    return render_template('studentlogin.html')


if __name__ == '__main__':
    app.run(debug=True)
