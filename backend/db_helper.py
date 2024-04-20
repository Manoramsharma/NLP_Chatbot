import mysql.connector

global cnx

# Database connection setup
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="recruitment_platform"  # Changed to a relevant database name
)

# Function to fetch job listings based on job type
def fetch_job_listings(job_type=None):
    cursor = cnx.cursor()
    query = "SELECT * FROM jobs WHERE job_type LIKE %s" if job_type else "SELECT * FROM jobs"
    cursor.execute(query, (f'%{job_type}%',) if job_type else ())
    results = cursor.fetchall()
    cursor.close()
    return results

# Function to fetch event details by name
def fetch_event_details(event_name):
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM events WHERE event_name = %s", (event_name,))
    result = cursor.fetchone()
    cursor.close()
    return result

# Function to check user registration for an event
def check_user_registration(user_id, event_name):
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM registrations WHERE user_id = %s AND event_name = %s", (user_id, event_name))
    result = cursor.fetchone()
    cursor.close()
    return bool(result)

# Function to update user progress in an event
def update_user_progress(user_id, event_name, progress):
    cursor = cnx.cursor()
    update_query = "UPDATE registrations SET progress = %s WHERE user_id = %s AND event_name = %s"
    cursor.execute(update_query, (progress, user_id, event_name))
    cnx.commit()
    cursor.close()

# Function to get personalized recommendations for a user
def get_recommendations(user_id):
    cursor = cnx.cursor()
    query = "SELECT recommendations FROM user_profiles WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    recommendations = cursor.fetchone()
    cursor.close()
    return recommendations

# Demo example: Establish a database connection
def demo_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="recruitment_platform"
        )
        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Successfully connected to MySQL database. MySQL Server version:", db_info)
            connection.close()
    except Exception as e:
        print(f"An error occurred while connecting to the database: {e}")

if __name__ == "__main__":
    # Example usage of the new functions
    print(fetch_job_listings('Software Developer'))
    print(fetch_event_details('CodeFest'))
    print(check_user_registration(101, 'CodeFest'))
    update_user_progress(101, 'CodeFest', 'Completed')
    print(get_recommendations(101))
    demo_db_connection()
