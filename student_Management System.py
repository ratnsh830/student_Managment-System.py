
import json
import os

students = []

# Load student data
def load_data():
    global students
    if os.path.exists("students.json"):
        with open("students.json", "r") as file:
            students = json.load(file)

# Save student data
def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

# Add Student
def add_student():
    roll = input("Enter Roll Number: ")

    for s in students:
        if s["roll"] == roll:
            print("Roll Number already exists!")
            return

    name = input("Enter Student Name: ")
    class_name = input("Enter Class: ")

    marks = []
    for i in range(1, 6):
        mark = float(input(f"Enter Subject {i} Marks: "))
        if mark < 0 or mark > 100:
            print("Marks must be between 0 and 100!")
            return
        marks.append(mark)

    student = {
        "roll": roll,
        "name": name,
        "class": class_name,
        "marks": marks
    }

    students.append(student)
    save_data()
    print("Student Added Successfully!")

# View Students
def view_students():
    if len(students) == 0:
        print("No Student Records Found!")
        return

    for s in students:
        print("\n----------------------")
        print("Roll Number:", s["roll"])
        print("Name:", s["name"])
        print("Class:", s["class"])
        print("Marks:", s["marks"])

# Search Student
def search_student():
    roll = input("Enter Roll Number: ")

    for s in students:
        if s["roll"] == roll:
            print("\nStudent Found!")
            print("Name:", s["name"])
            print("Class:", s["class"])
            print("Marks:", s["marks"])
            return

    print("Student Not Found!")

# Update Student
def update_student():
    roll = input("Enter Roll Number: ")

    for s in students:
        if s["roll"] == roll:
            s["name"] = input("Enter New Name: ")
            s["class"] = input("Enter New Class: ")
            save_data()
            print("Student Updated Successfully!")
            return

    print("Student Not Found!")

# Delete Student
def delete_student():
    roll = input("Enter Roll Number: ")

    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            save_data()
            print("Student Deleted Successfully!")
            return

    print("Student Not Found!")

# Calculate Result
def calculate_result():
    roll = input("Enter Roll Number: ")

    for s in students:
        if s["roll"] == roll:
            total = sum(s["marks"])
            percentage = total / 5

            if percentage >= 90:
                grade = "A+"
            elif percentage >= 80:
                grade = "A"
            elif percentage >= 70:
                grade = "B"
            elif percentage >= 60:
                grade = "C"
            elif percentage >= 40:
                grade = "D"
            else:
                grade = "Fail"

            print("\n----- STUDENT RESULT -----")
            print("Name:", s["name"])
            print("Total Marks:", total, "/ 500")
            print("Percentage:", percentage, "%")
            print("Grade:", grade)
            return

    print("Student Not Found!")

# Main Menu
def main():
    load_data()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Calculate Result")
        print("7. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            calculate_result()
        elif choice == "7":
            print("Thank You!")
            break
        else:
            print("Invalid Choice!")

main()
