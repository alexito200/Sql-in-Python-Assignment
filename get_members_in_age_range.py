from sql_in_python import connect_database
from mysql.connector import Error

def get_members_in_age_range(start_age, end_age):
    conn = connect_database()
    cursor = conn.cursor()
    # SQL query using BETWEEN
    try:
        query = "SELECT * FROM Members WHERE age BETWEEN %s AND %s;"

    # Execute and fetch results
        cursor.execute(query, (start_age, end_age))
        for row in cursor.fetchall():
            print(row)
        print('Code successfully passed')
    # Error handling
    except Error as e:
        print(f'Error: {e}')
    # Closing 
    finally:
        cursor.close()
        conn.close()

# Calling the function
get_members_in_age_range(25, 30)