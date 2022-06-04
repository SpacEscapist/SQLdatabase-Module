# Import functions file
from functions import *

# ===============================================

# Initialize "menu" variable
menu = "0"

# ===============================================

# Run "while" loop to present user with menu
while (menu != "7"):
    # Menu Options
    print("\n===========\nMain Menu\n===========\n\nPlease make a selection:\n-----------------------------")
    print("1. Add Student\n2. View All Students\n3. Modify Student Record\n4. Remove Student Record\n5. Sort Student Records\n6. Numeric Data about Students\n7. Quit Program")

    # Ask user input regarding Menu options
    menu = input("\n-> ")

    # ======================================================================================================================================

    # Add Student
    if (menu == "1"):
        print("\n============\nAdd Student\n============\n")
        studId = input("Student's ID: ")
        studFirst = input("Student's First Name: ")
        studLast = input("Student's Last Name: ")
        studGrade = input("Student's Grade Level: ")
        studGpa = input("Student's GPA: ")
        # Call addStudent function
        addStudent(studId, studFirst, studLast, studGrade, studGpa)
        # Arbitrary variable used to allow the user to look over the data table before pressing ENTER to continue to Main Menu
        x = input("\nPress ENTER to Continue")

    # ======================================================================================================================================

    # View Students
    elif (menu == "2"):
        print("\n==================\nView All Students\n==================")
        # Show user the student records
        viewStudents()
        # Arbitrary variable used to allow the user to look over the data table before pressing ENTER to continue to Main Menu
        x = input("\nPress ENTER to Continue")

    # ======================================================================================================================================

    # Modify Student Record
    elif (menu == "3"):
        print("\n=======================\nModify Student Record\n=======================")
        # Show user the student records
        viewStudents()
        # Ask user for student ID number that they wish to modify
        print("\nEnter Student ID# of the record you wish to MODIFY:")

        modifyStudentId = input("-> ")
        # Initialize user input variable
        modifyInput = 0
        while (modifyInput != 5):
            print("\nWhat do you want to MODIFY?\n-----------------------------")
            print("1. Student's First Name\n2. Student's Last Name\n3. Student's Grade Level\n4. Student's GPA\n5. DONE")
            modifyInput = input("\n-> ")

            # Student's First Name
            if modifyInput == "1":
                modifyColumn = "student_firstname"
                modifyDetails = input("\nNew First Name: ")
                modifyRecord(modifyColumn, modifyStudentId, modifyDetails)

            # Student's Last Name
            elif modifyInput == "2":
                modifyColumn = "student_lastname"
                modifyDetails = input("\nNew Last Name: ")
                modifyRecord(modifyColumn, modifyStudentId, modifyDetails)

            # Student's Grade Level
            elif modifyInput == "3":
                modifyColumn = "student_grade"
                modifyDetails = input("\nNew Grade Level: ")
                modifyRecord(modifyColumn, modifyStudentId, modifyDetails)

            # Student's GPA
            elif modifyInput == "4":
                modifyColumn = "student_gpa"
                modifyDetails = input("\nNew GPA: ")
                modifyRecord(modifyColumn, modifyStudentId, modifyDetails)

            # Leave Modify Student Record menu
            elif modifyInput == "5":
                break

            # Catch inputs outside of menu parameters
            else:
                print(
                    "\n==============================\nPlease enter a valid option\n==============================")

    # ======================================================================================================================================

    # Remove Student Record
    elif (menu == "4"):
        print("\n===============\nRemove Student\n===============")
        # Show user the student records
        viewStudents()
        removeStudentId = input(
            "\nEnter Student ID# of the record you wish to REMOVE: ")
        # Call removeRecord function
        removeRecord(removeStudentId)
        # Arbitrary variable used to allow the user to look over the data table before pressing ENTER to continue to Main Menu
        x = input("\nPress ENTER to Continue")

    # ======================================================================================================================================

    # Sort Records
    elif (menu == "5"):
        print("\n======================\nSort Student Records\n======================")
        # Show user the student records
        viewStudents()
        print("\nWhat COLUMN would you like to sort by?\n----------------------------------------")
        print("1. Student ID\n2. Student's First Name\n3. Student's Last Name\n4. Student's Grade Level\n5. Student's GPA")

        # Ask user for column they want to sort by
        columnSort = input("\n-> ")
        if (columnSort == "1"):
            columnSort = "student_id"
        elif (columnSort == "2"):
            columnSort = "student_firstname"
        elif (columnSort == "3"):
            columnSort = "student_lastname"
        elif (columnSort == "4"):
            columnSort = "student_grade"
        elif (columnSort == "5"):
            columnSort = "student_gpa"

        print("\nWhat ORDER would you like to sort by?\n----------------------------------------")
        print("1. Ascending\n2. Descending")

        # Ask user for order they want to sort by
        orderSort = input("\n-> ")
        if (orderSort == "1"):
            orderSort = "ASC"
        elif (orderSort == "2"):
            orderSort = "DESC"

        # Call the sortData function
        sortData(columnSort, orderSort)

        # Arbitrary variable used to allow the user to look over the data table before pressing ENTER to continue to Main Menu
        x = input("\nPress ENTER to Continue")

    # ======================================================================================================================================

    # Get numeric data about database
    elif (menu == "6"):
        print("\n===============\nNumeric Data\n===============")
        numericData()

        # Arbitrary variable used to allow the user to look over the data table before pressing ENTER to continue to Main Menu
        x = input("\n\nPress ENTER to Continue")

    # ======================================================================================================================================

    # Quit Program
    elif (menu == "7"):
        quitProgram()

    # ======================================================================================================================================

    # Catch inputs outside of menu parameters
    else:
        print("\n==============================\nPlease enter a valid option\n==============================")
