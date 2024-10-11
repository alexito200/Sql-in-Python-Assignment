from sql_in_python import connect_database
from mysql.connector import Error

def update_member_age(member_id, new_age):
    conn = connect_database()
    cursor = conn.cursor()

    # SQL query to update age
    try:
        query = '''UPDATE Members SET age = %s WHERE id = %s'''

        cursor.execute(query, (new_age, member_id))
        conn.commit()
        print('Age for member successfully updated!')

    # Check if member exists
    except Error as e:
        print(f'Error: {e}')
        print('Member with this ID does not exist or other constraint violation')
    finally:
        cursor.close()
        conn.close()

# Example usage
update_member_age(4, 52)