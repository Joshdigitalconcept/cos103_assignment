# Write a program that reads a text file and counts the number of words, lines, and characters.
def count_file_stats(filename):
    with open(filename, 'r') as file:
        content = file.read()
        lines = content.splitlines()
        words = content.split()
        characters = len(content)

    return len(lines), len(words), characters

# Example usage
filename = input("Enter the filename: ")
lines, words, characters = count_file_stats(filename)
print(f"Lines: {lines}, Words: {words}, Characters: {characters}")

# Create a simple student database that allows adding, viewing, and deleting student records stored in a file.
import json

def load_students():
    try:
        with open("students.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_students(students):
    with open("students.json", "w") as file:
        json.dump(students, file)

def add_student(name, age, grade):
    students = load_students()
    students.append({"name": name, "age": age, "grade": grade})
    save_students(students)

def view_students():
    students = load_students()
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

def delete_student(name):
    students = load_students()
    students = [student for student in students if student["name"] != name]
    save_students(students)

# Example usage
while True:
    print("\nStudent Database Menu:")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        grade = input("Enter student grade: ")
        add_student(name, age, grade)
        print("Student added successfully.")

    elif choice == "2":
        view_students()

    elif choice == "3":
        name = input("Enter the name of the student to delete: ")
        delete_student(name)
        print("Student deleted successfully.")

    elif choice == "4":
        break

    else:
        print("Invalid choice. Please try again.")

