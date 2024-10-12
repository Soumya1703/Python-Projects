import random


def roll_dice(num_dice):
    results = [random.randint(1, 6) for _ in range(num_dice)]
    for result in results:
        print(result, end=" ")


def get_number_of_dice():
    while True:
        try:
            return int(input("How many dice you want to roll: "))
        except ValueError as e:
            print("Please enter a valid number")


def main():
    print("---Welcome to the Roll Dice---")
    while True:
        num_dice = get_number_of_dice()
        roll_dice(num_dice)
        roll_again = input("\nDo you want to roll again? (yes/no)\n").strip().lower()
        if roll_again != "yes":
            print("Thanks for playing")
            break


if __name__ == "__main__":
    main()