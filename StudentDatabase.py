import numpy as np
import Prints


student_dtype = np.dtype([
    ('index', 'i4'),
    ('name', 'U50'),
    ('mid_grade', 'f4'),
    ('end_grade', 'f4'),
    ('total_grade', 'f4'),
    ('status', 'U10')
])


student_database = np.empty(0, dtype=student_dtype)


def add_student(name, mid_grade, end_grade):
    global student_database

    total_grade = (mid_grade + end_grade) / 2
    status = "passed" if total_grade >= 75 else "failed"
    index = len(student_database) + 1

    new_student = np.array([(index, name, mid_grade, end_grade, total_grade, status)], dtype=student_dtype)

    student_database = np.append(student_database, new_student)


def delete_student(index):
    global student_database
    if 1 <= index <= len(student_database):
        student_database = student_database[student_database['index'] != index]

        for i in range(len(student_database)):
            student_database[i]['index'] = i + 1
    else:
        print("Invalid index number.")


def update_student(index):
    global student_database
    if 1 <= index <= len(student_database):
        indexlookup = index - 1
        student_database[indexlookup]['name'] = input("Enter Name: ")
        student_database[indexlookup]['mid_grade'] = float(input("Enter Midterm Grade: "))
        student_database[indexlookup]['end_grade'] = float(input("Enter Endterm Grade: "))
        total_grade = (student_database[indexlookup]['mid_grade'] + student_database[indexlookup]['end_grade']) / 2
        student_database[indexlookup]['total_grade'] = total_grade
        student_database[indexlookup]['status'] = "passed" if total_grade >= 75 else "failed"
    else:
        print("Invalid index number.")


def display_studentdatabase():
    if len(student_database) == 0:
        print("The database is empty.")
    else:
        print(student_database)


def database_interface():
    while True:
        print("\nOptions:")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Display Database")
        print("4. Return to Main")
        print("5. Update Student")
        print("0. Exit Program")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter student's name: ")
            mid_grade = float(input("Enter midterm grade: "))
            end_grade = float(input("Enter endterm grade: "))
            add_student(name, mid_grade, end_grade)
            print(f"Student {name} added successfully.")

        elif choice == 2:
            index = int(input("Enter the index number of the student to delete: "))
            delete_student(index)
            print(f"Student at index {index} deleted successfully.")

        elif choice == 3:
            display_studentdatabase()

        elif choice == 4:
            print("Returning to Main")
            Prints.OptionsMenu()
        elif choice == 5:
            index = int(input("Enter the index number of the student to Update: "))
            update_student(index)

        elif choice == 0:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")
