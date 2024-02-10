import random
print("words are apple , banana ,watermelon ,grape , orange")
def hangman():
    words = ["apple", "banana", "orange", "grape", "watermelon"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        display = ""
        for letter in word:
            if letter in guessed_letters:
                display += letter
            else:
                display += "_"
        print(display)

        if display == word:
            print("Congratulations! You guessed the word.")
            break

        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
        else:
            print("Incorrect guess.")
            attempts -= 1
            print(f"Attempts left: {attempts}")

    if attempts == 0:
        print(f"Sorry, you ran out of attempts. The word was '{word}'.")

hangman()
