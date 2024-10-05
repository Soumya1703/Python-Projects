import random

number = random.randint(0, 10)

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 0 and 100. Can you guess what it is?")

while True:
    user_input = None
    try:
        user_input = int(input("Please guess the number: "))
    except ValueError as e:
        print("Please enter a valid number")
        continue
    if user_input < number:
        print("Too Low. Please try again.")

    elif user_input > number:
        print("Too High. Please try again.")

    else:
        print("Congratulation!!! You guessed the number correctly.")
        break

    