from sql_in_python import connect_database
from mysql.connector import Error

def delete_workout_session(session_id, member_id):
    conn = connect_database()
    cursor = conn.cursor()

    # SQL query to delete a session
    try:
        query = "DELETE FROM WorkoutSessions WHERE session_id = %s AND member_id = %s"

        cursor.execute(query, (session_id, member_id))
        conn.commit()
        print('Workout session deleted')

    # Error handling for non-existent session ID
    except Error as e:
        print(f'Error: {e}')
        print('Member with this ID does not exist or other constraint violation')

    finally:
        cursor.close()
        conn.close()

delete_workout_session(2, 2)