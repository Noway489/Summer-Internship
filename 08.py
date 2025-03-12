import psycopg2

host = 'localhost'
database = 'my_database'
user = 'postgres'
password = 'Sanskar@12'

try: 
    conn = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conn.cursor()
    
    # Update single record
    sql_update_query = """UPDATE student SET id = %s WHERE 'name' = %s"""
    id_value = 3  # Replace with the actual ID value
    name_value = 'Golu'  # Replace with the actual name
    cursor.execute(sql_update_query, (id_value, name_value))
                        
    conn.commit()
    count = cursor.rowcount
    print(count, "Record(s) updated successfully.")
    
except (Exception, psycopg2.Error) as error:
    print("Error in update operation:", error)
 
finally:
    # Closing database connection
    if conn:
        cursor.close()
        conn.close()
        print("PostgreSQL connection is closed.")
Id = 3
 = 2000
updateTable(publisherId, establishedYear)        
