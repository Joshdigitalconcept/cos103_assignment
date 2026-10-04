# Implement a contact book using a dictionary
contacts = {}

def add_contact(name, phone):
    contacts[name] = phone

def get_contact(name):
    return contacts.get(name, "Contact not found")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
    else:
        print("Contact not found")

def display_contacts():
    if contacts:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts found")

# Main program
while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. Get Contact")
    print("3. Delete Contact")
    print("4. Display Contacts")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        add_contact(name, phone)
        print(f"Contact {name} added.")
    elif choice == "2":
        name = input("Enter contact name to retrieve: ")
        print(get_contact(name))
    elif choice == "3":
        name = input("Enter contact name to delete: ")
        delete_contact(name)
    elif choice == "4":
        display_contacts()
    elif choice == "5":
        print("Exiting the contact book.")
        break
    else:
        print("Invalid choice. Please try again.")

# Create a program that reads a list of students names and scores, then output the highest score, average score, and all names in alphabetical order.
students = []

while True:
    name = input("Enter student name (or 'done' to finish): ")
    if name == "done":
        break
    score = float(input("Enter student score: "))
    students.append((name, score))

if students:
    names = [student[0] for student in students]
    scores = [student[1] for student in students]

    print(f"Names in alphabetical order: {sorted(names)}")
    print(f"Highest score: {max(scores)}")
    print(f"Average score: {sum(scores) / len(scores):.2f}")
else:
    print("No students added.")