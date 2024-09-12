import numpy as np


class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.subjects = np.array([], dtype=object)


class Subject:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class StudentManagementSystem:
    def __init__(self):
        self.students = np.array([], dtype=object)
        self.subjects = np.array([], dtype=object)

    def add_student(self):
        name = input("Enter student name: ")
        id = input("Enter student ID: ")
        student = Student(name, id)
        self.students = np.append(self.students, student)
        print(f"Student {name} added successfully.")

    def add_subject(self):
        name = input("Enter subject name: ")
        code = input("Enter subject code: ")
        subject = Subject(name, code)
        self.subjects = np.append(self.subjects, subject)
        print(f"Subject {name} added successfully.")

    def enroll_student(self):
        student_id = input("Enter student ID: ")
        subject_code = input("Enter subject code: ")

        student = np.array([s for s in self.students if s.id == student_id])
        subject = np.array([s for s in self.subjects if s.code == subject_code])

        if student.size > 0 and subject.size > 0:
            student[0].subjects = np.append(student[0].subjects, subject[0])
            print(f"Student {student[0].name} enrolled in {subject[0].name}.")
        else:
            print("Student or subject not found.")

    def display_course_list(self):
        for subject in self.subjects:
            print(f"Subject: {subject.name}, Code: {subject.code}")

    def run(self):
        while True:
            print("\n1. Add Student")
            print("2. Add Subject")
            print("3. Enroll Student")
            print("4. Display Course List")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.add_subject()
            elif choice == '3':
                self.enroll_student()
            elif choice == '4':
                self.display_course_list()
            elif choice == '5':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    sms = StudentManagementSystem()
    sms.run()