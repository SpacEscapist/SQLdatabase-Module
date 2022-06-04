# Import SQLite library
import sqlite3

# Create a connection to the database and sets it to a variable
# If database name does not exists, it creates a new database with the name specified
connection = sqlite3.connect("hs-students.db")

# -----------------------------------------------------------------------------------------------------

# Create a cursor (A cursor allows you to interact with the database and perform commands)
c = connection.cursor()

# -----------------------------------------------------------------------------------------------------

# # Create a table in the database (One-Time only)
# # Once the table has been created, COMMENT OUT or DELETE this code.
# c.execute("""CREATE TABLE students (
#     student_id integer,
#     student_firstname text,
#     student_lastname text,
#     student_grade integer,
#     student_gpa real
# )""")

# -----------------------------------------------------------------------------------------------------


# Performs user action/SQL statement on database and commits their action
def userInteraction(input):
    # Executes user action
    c.execute(input)
    # Commits and "pushes" the command to the database
    connection.commit()
