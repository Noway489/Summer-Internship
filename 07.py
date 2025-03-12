import pyodbc
server = 'NOWAY489'
database = 'MY_DAtabase23'
username = 'dbo'
password = 'admin'
conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database}U;ID={username};PWD={password}'

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
cursor.execute('SELECT * FROM your_table')
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
conn.close()
