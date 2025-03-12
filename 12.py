import psycopg2
from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['GET'])
def submit():
    print("hit")
    host = 'localhost'
    database = 'my_database'
    user = 'postgres'
    password = 'Sanskar@12'
    conn = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conn.cursor()

    try:
        conn = psycopg2.connect(host=host, database=database, user=user, password=password)
        cursor = conn.cursor()

        # Retrieve form data
        name = request.form['name']
        email = request.form['email']
        # Retrieve other form fields as needed

        # Insert data into the database table
        sql = f"INSERT INTO question_form(name, email) VALUES ('{name}', '{email}')"
        cursor.execute(sql)
        conn.commit()
        print("Data inserted successfully.")
    except (Exception, psycopg2.Error) as error:
        print("Error in insert operation:", error)
    finally:
        # Closing database connection.
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed.")

    # Return a response to the client
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run()
