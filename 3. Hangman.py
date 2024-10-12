import random


def run_game():
    word_list = ["ball", "death", "die", "hi"]
    word = random.choice(word_list)

    username = input("Your name is: ").capitalize()
    print(f"Welcome to the Hangman game, {username}!")
    dashes = " ".join(["_" for char in range(len(word))])
    print(f"The selected word is: {dashes}")
    print("You can start guessing the word!")

    guessed = ""
    chances = 5

    while chances > 0:
        attempts = 0
        print("Word: ", end="")
        for char in word:
            if char in guessed:
                print(char, end=" ")
            else:
                print("", end=" ")
                attempts += 1
        print()  # Add a blank line

        if attempts == 0:
            print("Congratulations! You've guessed the word correctly.")
            break

        # Input validation to ensure only one letter is entered
        while True:
            guess = input("Enter a letter: ").lower()
            if len(guess) == 1 and guess.isalpha():
                break
            else:
                print("Invalid input. Please enter a single letter.")

            if guess in guessed:
                print(f"You already guessed '{guess}'. Try another letter.")
            elif guess in word:
                guessed += guess
                print(f"Good job! '{guess}' is in the word.")
            else:
                chances -= 1
                print(
                    f"Sorry, '{guess}' is not in the word. You have {chances} chances left."
                )
                if chances == 0:
                    print(f"Game over! The word was '{word}'.")


if __name__ == "_main_":
    run_game()
