import psycopg2

def updateTable(id, Name):
    host = 'localhost'
    database = 'my_database'
    user = 'postgres'
    password = 'Sanskar@12'

    try: 
        conn = psycopg2.connect(host=host, database=database, user=user, password=password)
        cursor = conn.cursor()
        
        # Update single record
        sql_update_query = """UPDATE student2 SET "Name" = %s WHERE "id" = %s"""
        id_value = id # Replace with the actual ID value
        name_value = Name # Replace with the actual name
        cursor.execute(sql_update_query, (name_value, id_value))
                            
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

# Call the update function
studentId = 9
studentName = 'Sanskar'
updateTable(studentId, studentName)
