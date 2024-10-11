from sql_in_python import connect_database
from mysql.connector import Error

def add_workout_session(session_id, member_id, session_date, duration_minutes, calories_burned):
    try:
        conn = connect_database()  # Try to connect to the database
        cursor = conn.cursor()

        # SQL query to add a new workout session
        query = '''INSERT INTO WorkoutSessions (session_id, member_id, session_date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s, %s)'''

        # Execute the query with the provided values
        cursor.execute(query, (session_id, member_id, session_date, duration_minutes, calories_burned))
        conn.commit()
        print('Workout session successfully added!')

    # Error handling
    except Error as e:
        print(f'Error: {e}')
        print('Error adding workout session: Possible invalid member ID or constraint violation')

    finally:
        # Ensure both cursor and connection are closed properly
            cursor.close()
            conn.close()

# Example usage
add_workout_session(3, 4, '2024-10-11', 60, 500)
