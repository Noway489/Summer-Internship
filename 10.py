import psycopg2

host = 'localhost'
database = 'my_database'
user = 'postgres'
password = 'Sanskar@12'

try:
    conn = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conn.cursor()
    
    create_table_query = """
        CREATE TABLE IF NOT EXISTS student3 ( id SERIAL PRIMARY KEY, Name Char, Roll_No Integer )"""
    
    cursor.execute(create_table_query)

    # Commit the transaction
    conn.commit()
except (Exception, psycopg2.Error) as error:
    print("Error in table creation:", error)
finally:
    # Closing database connection
    if conn:
        cursor.close()
        conn.close()
        print("PostgreSQL connection is closed.")
