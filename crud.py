import psycopg2

DB_CONFIG = {
    "dbname": "school",
    "user": "postgres", # replace with your PostgreSQL username
    "password": "password", # replace with your PostgreSQL password
    "host": "localhost",
    "port": "5432"
}

try:
    db_connection = psycopg2.connect(**DB_CONFIG)
except:
    print("Unable to connect to the database.")
cursor = db_connection.cursor()

# Retrieves and displays all records from the students table
def getAllStudents():
    if db_connection:
        cursor.execute("SELECT * FROM students ORDER BY student_id;")
        rows = cursor.fetchall()
        print("\nStudents:")
        for row in rows:
            print(row)

# Inserts a new student record into the students table
def addStudent(first_name, last_name, email, enrollment_date):
    if db_connection:
        query = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);"
        cursor.execute(query, (first_name, last_name, email, enrollment_date))
        db_connection.commit()
        print(f"Added student!")

# Updates the email address for a student with the specified student_id
def updateStudentEmail(student_id, new_email):
    if db_connection:
        query = "UPDATE students SET email = %s WHERE student_id = %s;"
        cursor.execute(query, (new_email, student_id))
        db_connection.commit()
        if cursor.rowcount > 0:
            print(f"Email updated for student ID {student_id}")
        else:
            print(f"No student found with ID {student_id}")

# Deletes the record of the student with the specified student_id
def deleteStudent(student_id):
    if db_connection:
        query = "DELETE FROM students WHERE student_id = %s;"
        cursor.execute(query, (student_id,))
        db_connection.commit()
        if cursor.rowcount > 0:
            print(f"Deleted student ID {student_id}")
        else:
            print(f"No student found with ID {student_id}")

def main():
    getAllStudents()

    # addStudent('mary', 'brown', 'marybrown@cmail.carleton.ca', '2023-01-01')
    # getAllStudents()

    # updateStudentEmail(4, 'newemail@example.com')
    # getAllStudents()

    # deleteStudent(4)
    # getAllStudents()

    cursor.close()
    db_connection.close()

main()