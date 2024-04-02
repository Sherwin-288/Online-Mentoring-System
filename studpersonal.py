from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

@app.route('/')
def registration_form():
    return render_template('studpersonal.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        try:
            submitted_data = request.form.to_dict()
            return render_template('confirmation.html', data=submitted_data)
        except Exception as e:
            return str(e)
    else:
        return redirect(url_for('registration_form'))

@app.route('/confirm', methods=['POST'])
def confirm():
    if request.method == 'POST':
        submitted_data = request.form.to_dict()
        confirm_action = submitted_data.get('confirm')
        if confirm_action == 'yes':
            try:
                connection = pymysql.connect(host='localhost',
                                             user='root',
                                             password='sherwin@288',
                                             database='test',
                                             cursorclass=pymysql.cursors.DictCursor)

                with connection.cursor() as cursor:
                    sql = "INSERT INTO regst (name, roll_no, dob, gender, addr, mno1, mail1, fname, mno2, mail2, mname, mno3, mail3, facname, dsg, dept, mentname, mno4, mail4) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    cursor.execute(sql, (
                        submitted_data['name'], submitted_data['roll_no'], submitted_data['dob'],
                        submitted_data['gender'], submitted_data['addr'], submitted_data['mno1'],
                        submitted_data['mail1'], submitted_data['fname'], submitted_data['mno2'],
                        submitted_data['mail2'], submitted_data['mname'], submitted_data['mno3'],
                        submitted_data['mail3'], submitted_data['facname'], submitted_data['dsg'],
                        submitted_data['dept'], submitted_data['mentname'], submitted_data['mno4'],
                        submitted_data['mail4']))

                connection.commit()
                return "You've successfully filled the registration form!!"
            except Exception as e:
                return str(e)
            finally:
                if 'connection' in locals():
                    connection.close()
        else:
            return redirect(url_for('registration_form'))

if __name__ == '__main__':
    app.run(debug=True)