# Write a program that determines if a number is positive, negative, or zero.
user_num = float(input("Enter a number: "))
if user_num > 0:
    print(f"{user_num} is a positive number.")
elif user_num < 0:
    print(f"{user_num} is a negative number.")
elif user_num == 0:
    print(f"{user_num} is zero.")
else:
    print("Please enter a valid number.")

# Create a password strength checker
password = input("Enter a password: ")
if len(password) < 6:
    print("Weak password: Password must be at least 6 characters long.")
elif not any(char.isdigit() for char in password):
    print("Weak password: Password must contain at least one digit.")
elif not any(char.isupper() for char in password):
    print("Weak password: Password must contain at least one uppercase letter.")
elif not any(char.islower() for char in password):
    print("Weak password: Password must contain at least one lowercase letter.")
else:
    print("Strong password: Your password is strong.")

# Develop a simple grading system that assigns grades based on input scores.
score = float(input("Enter the student's score: "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"The student's grade is: {grade}")