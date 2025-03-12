import psycopg2

def deleteTable(id):
    host = 'localhost'
    database = 'my_database'
    user = 'postgres'
    password = 'Sanskar@12'

    try: 
        conn = psycopg2.connect(host=host, database=database, user=user, password=password)
        cursor = conn.cursor()
        delete_table_Query="Delete From Student2 Where id=%s"
        cursor.execute(delete_table_Query, (id,))
        conn.commit()
        count = cursor.rowcount
        print(count, "Record deleted successfully ")
 
    except (Exception, psycopg2.Error) as error:
        print("Error in Delete operation", error)
 
    finally:
        # closing database connection.
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")
 
 
id = 8
deleteTable(id)