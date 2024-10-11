from sql_in_python import connect_database
from mysql.connector import Error

conn = connect_database()

def add_member(id, name, age):
    cursor = conn.cursor()

    try:
        # SQL query to add a new member

        query = 'INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)'

        cursor.execute(query, (id, name, age))
        conn.commit()
        print('New member added')
        # Error handling for duplicate IDs or other constraints
    except Error as e:
        print(f'Error: {e}')
        print('Member with this ID already exists or there is a constraint violation')
    finally:
        cursor.close()
        conn.close()

add_member(3, 'Nicholas', 23)