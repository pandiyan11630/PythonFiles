import cx_Oracle

username = "Raavanan"
password = "Pandiyan#123"
connectionString = "localhost:1521/orcl"

# Establish a connection to the database
connection = cx_Oracle.connect(username, password, connectionString)
cursor = connection.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE employees6056 (
        id NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY,
        name VARCHAR2(50),
        age NUMBER,
        salary NUMBER,
        PRIMARY KEY (id)
    )
''')
connection.commit()

