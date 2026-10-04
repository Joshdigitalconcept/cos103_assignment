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