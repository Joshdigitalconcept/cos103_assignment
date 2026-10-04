# Write a program that prints all prime numbers up to a given number
number = int(input("Enter a number: "))

for num in range(2, number + 1):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)

# Create a multiplication table using nested loops
user_num = int(input("Multiplication table for which number: "))
rows = int(input("How many times? "))

for i in range(1, rows + 1):
    for row in range(1, 2):
        print(f"{user_num} * {i} = {user_num * i}")

# Develop a simple number guessing game
import random

secret_number = random.randint(1, 100)

while True:
    guess = int(input("Guess the number (1-100): "))

    if guess == secret_number:
        print("Correct! You guessed the number!")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")