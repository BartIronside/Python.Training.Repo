import random 

options = ("rock", "paper", "scissors")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("What's your move? Enter your choice: ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    else:
        print("You lose!")
    

    while True:
        again = input("Wanna play again? (y/n): ").lower()
        if again == "y":
            break
        elif again == "n":
            running = False
            print("Thank you for the game!")
            break
        else:
            print("Incorrect choice. Choose y or n")