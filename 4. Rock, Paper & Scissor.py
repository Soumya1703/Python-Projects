import random


def run_game():
    options = ["rock", "paper", "scissors"]
    symbols = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}
    username = input("Your name is: ").capitalize()
    print(f"Welcome to the Rock, Paper, Scissors Game, {username}!")
    user_score = 0
    AI_score = 0
    while True:
        user = input(
            "Choose one -> Rock, Paper or Scissors (or type 'exit' to quit): "
        ).lower()

        if user == "exit":
            print("Thanks for Playing.")
            break
        if user not in options:
            print("Invalid input. Please choose between Rock, Paper, or Scissors.")
            continue
        AI = random.choice(options)
        print(f"You: {symbols[user]}")
        print(f"AI: {symbols[AI]}")
        if user == AI:
            print("It's a Tie!!!")
        elif (
            (user == "rock" and AI == "scissors")
            or (user == "scissors" and AI == "paper")
            or (user == "paper" and AI == "rock")
        ):
            print("You Win!!!")
            user_score += 1
        else:
            print("You Lose!!!")
            AI_score += 1
            print(f"**Final Scores**\nYou: {user_score}, AI: {AI_score}")


if __name__ == "_main_":
    run_game()
