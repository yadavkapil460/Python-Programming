import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Choose a difficulty level: easy, medium, hard")

    levels = {
        "easy": 10,
        "medium": 6,
        "hard": 3
    }

    level = input().lower()
    if level not in levels:
        print("Invalid level. Please choose from easy, medium, or hard.")
        return

    print(f"You chose {level} level. You have {levels[level]} attempts.")

    number = random.randint(1, 100)
    attempts = levels[level]

    while attempts > 0:
        guess = int(input("Enter your guess (between 1 and 100): "))
        attempts -= 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {number} in {levels[level] - attempts} attempts.")
            break

        if attempts > 0:
            print(f"Attempts left: {attempts}")
        else:
            print(f"Sorry, you ran out of attempts. The number was {number}.")

number_guessing_game()
