# Overview

This program is used to mimic software that a school faculty member might use for their students. An SQL Relational Database is used to store student data - their student ID, first and last name, grade level, and GPA. This program allows the user to perform CRUD operations on the student record data through the use of a Main Menu presented in the program. Through the Main Menu, the software uses a variety of INSERT, SELECT, UPDATE, and DELETE SQL statements to perform the necessary actions based on what options the user selects.

Most of the Main Menu options are self-explanatory, I will explain a few options in more detail.
The Main Menu consists of:
Add Student
View All Students
Modify Student Record - Allows user to edit all student record data except for Student ID
Remove Student Record
Sort Student Records - Allows user to select which column they wish to sort by, and if they want Ascending or Descending order
Get Numeric Data about Students - This shows the user the overall number of students in the table, as well as the AVERAGE gpa among all students
Quit Program

The purpose for creating this program was to showcase my understanding of SQL databases, SQL commands, and how to interact with that database using Python. This software was also created to test my ability to learn the code and implement a working program within a short period of time (2 weeks).

[Software Demo Video](https://youtu.be/8FWZK8OPkeE)

# Relational Database

I'm using a SQLite3 database, and using Python to execute commands to the SQL database.
The table name is: students, and the table consists of 5 columns:
student_id
student_firstname
student_lastname
student_grade
student_gpa

student_firstname and student_lastname hold TEXT values
student_id and student_grade hold INTEGER values
student_gpa holds REAL values

At this point in time, the database utilizes only 1 table to contain all the student data.

# Development Environment

Visual Studio Code
Git / GitHub

Python
SQLite3
Pandas

# Useful Websites

- [YouTube](https://www.youtube.com/)
- [Stack Overflow](https://stackoverflow.com/)
- [SQLite Tutorial](https://www.sqlitetutorial.net/)
- [W3Schools SQL Tutorial](https://www.w3schools.com/sql/)

# Future Work

- Add: New table to test myself and increase depth/content of the program
- Improve: Additional error catching, to prevent program from crashing if user selects outside of menu option parameters
- Add: Additional menu options to allow user more choices to manipulate data
