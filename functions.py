# Import database file
from database import *
# Import Pandas Library
import pandas as pd

# ======================================================================================================================================


# Add Student
def addStudent(studId, studFirst, studLast, studGrade, studGpa):
    # INSERT statement
    output = f"INSERT INTO students VALUES ('{studId}', '{studFirst}', '{studLast}', '{studGrade}', '{studGpa}')"
    # Send user SQL statement to the database file
    userInteraction(output)
    print(
        f"\n--------------------------------------------------\nStudent record for {studFirst} {studLast} has been ADDED.\n--------------------------------------------------\n")

# ======================================================================================================================================


# View ALL Students
def viewStudents():
    print("\n=============================================================================")
    # Use Pandas Library to display data table in a nice format
    print(pd.read_sql_query(
        "SELECT * FROM students", connection, index_col="student_id"))
    print("=============================================================================\n")

# ======================================================================================================================================


# Edit/Modify Student Record
def modifyRecord(modifyColumn, modifyStudentId, modifyDetails):

    # UPDATE statement
    output = f"UPDATE students SET {modifyColumn} = '{modifyDetails}' WHERE student_id = '{modifyStudentId}'"
    # Send user SQL statement to the database file
    userInteraction(output)

    # Inform user that the record was modified
    print(
        f"\n--------------------------------------\nStudent record has been MODIFIED\n--------------------------------------\n")


# ======================================================================================================================================


# Remove Student Record by student_id column
def removeRecord(removeStudentId):

    # DELETE statement by student_id
    output = f"DELETE FROM students WHERE student_id = '{removeStudentId}'"
    # Send user SQL statement to the database file
    userInteraction(output)

    # Inform user that the record was deleted
    print(
        f"\n-------------------------------------------------\nStudent record for ID# {removeStudentId} has been REMOVED\n-------------------------------------------------\n")

# ======================================================================================================================================


# Sort table data, specified by user
def sortData(columnSort, orderSort):

    # Inform user that the data was sorted
    print(
        f"\n---------------------------------\nStudent Data has been SORTED\n---------------------------------\n")

    # Sort the data table by parameters the user selected
    print("\n=============================================================================")
    # Use Pandas Library to display data table in a nice format
    print(pd.read_sql_query(
        f"SELECT * FROM students ORDER BY {columnSort} {orderSort}", connection, index_col="student_id"))
    print("=============================================================================\n")

# ======================================================================================================================================


# Get numeric data from database using aggregate functions to summarize data
def numericData():

    # SELECT statement using the COUNT function
    output1 = f"SELECT COUNT(*) FROM students"
    # Send user SQL statement to the database file
    userInteraction(output1)
    # Retrieve the query result set
    countStudents = c.fetchone()

    # SELECT statement using the AVG function
    output2 = f"SELECT AVG(student_gpa) FROM students"
    # Send user SQL statement to the database file
    userInteraction(output2)
    # Retrieve the query result set
    avgGpa = c.fetchone()

    # Loop through countStudents result set and pull out specific value (so data doesn't appear in a list)
    for total in countStudents:
        print(f"\n- Total number of Students: {total}")

    # Loop through avgGpa result set and pull out specific value (so data doesn't appear in a list)
    for avg in avgGpa:
        print(f"- Average GPA among Students: {avg}")


# ======================================================================================================================================


# Quit program and close the database connection
def quitProgram():
    print("\nQuitting Program...\n")
    connection.close()
