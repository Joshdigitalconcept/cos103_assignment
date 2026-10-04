value = input("Enter a word: ")

if value == value[::-1]:
    print(f"{value} is a palindrome.")
else:
    print(f"{value} is not a palindrome.")

print(value.capitalize())
print(value.upper())
print(value.lower())

# Hangman
word = "python"
guessed_word = "_" * len(word)
attempts = 6

print("Welcome to Hangman!")
print("Guess the word:", guessed_word)

while attempts > 0 and "_" in guessed_word:
    guess = input("Guess a letter: ")

    if guess in word:
        print("Correct!")

        new_word = ""

        for i in range(len(word)):
            if word[i] == guess:
                new_word += guess
            else:
                new_word += guessed_word[i]

        guessed_word = new_word

    else:
        attempts -= 1
        print("Wrong!")
        print("Attempts left:", attempts)

    print("Word:", guessed_word)

if "_" not in guessed_word:
    print("You won! 🎉")
else:
    print("You lost!")
    print("The word was:", word)
    