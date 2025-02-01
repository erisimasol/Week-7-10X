import mysql.connector
from mysql.connector import Error

try:
    # Establish a connection
    conn = mysql.connector.connect(
        host='127.0.0.1',            # e.g., 'localhost' or '127.0.0.1'
        user='root',                 # your MySQL username (typically 'root' without '@localhost')
        password='your_password',     # your MySQL password
        database='my_model'           # the database you want to connect to
    )

    # Check if the connection is successful
    if conn.is_connected():
        print("Connected to MySQL database")
    else:
        print("Connection failed")

except Error as e:
    print(f"Error: {e}")

finally:
    # Close the connection when done
    if conn.is_connected():
        conn.close()
        print("Connection closed")