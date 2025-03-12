from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

# PostgreSQL database connection settings
host = 'localhost'
database = 'my_database'
user = 'postgres'
password = 'Sanskar@12'

@app.route('/')
def index():
    return render_template('question.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    # Retrieve form data
    name = request.form['name']
    email = request.form['email']
    mobile = request.form['mobile']
    dob = request.form['dob']
    occupation = request.form['occupation']
    question = request.form['question']
    picture = request.form['picture']
    
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conn.cursor()

    try:
        # Insert data into the database table
        sql = "INSERT INTO question_form2 (name, email, mobile, dob, occupation, question, picture) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (name, email, mobile, dob, occupation, question, picture)
        cursor.execute(sql, values)
        conn.commit()
        print("Data inserted successfully.")
    except (Exception, psycopg2.Error) as error:
        print("Error inserting data:", error)
    finally:
        # Closing database connection
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed.")

    # Redirect to the display page and pass the entered data as a parameter
    return redirect(url_for('display_data', name=name, email=email, mobile=mobile, dob=dob, occupation=occupation, question=question, picture=picture))
    
@app.route('/display')
def display_data():
    # Retrieve data from the URL parameters
    name = request.args.get('name')
    email = request.args.get('email')
    mobile = request.args.get('mobile')
    dob = request.args.get('dob')
    occupation = request.args.get('occupation')
    question = request.args.get('question')
    picture = request.args.get('picture')

    # Render the HTML template with the retrieved data
    return render_template('display.html', name=name, email=email, mobile=mobile, dob=dob, occupation=occupation, question=question, picture=picture)

if __name__ == '__main__':
    app.run()
