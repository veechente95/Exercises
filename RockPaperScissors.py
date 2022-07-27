import random

while True:
    options = ["rock", "paper", "scissors"]
    computer = random.choice(options)
    player = None

    while player not in options:
        player = str(input("Please select rock, paper or scissors: ")).lower()

    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("It's a tie!")

    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You win")

    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose")
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You win")

    elif player == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You win")

    play_again = input("Would you like yo play again? (yes / no): ").lower()
    if play_again != "yes":
        break
print("Thank you! Bye")
