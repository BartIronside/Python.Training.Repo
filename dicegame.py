import random



#  ┌ ─  ┐ │ └ ┘


#"┌─────────┐"
#"│         │"
#"│         │"
#"│         │"
#"└─────────┘"

running = True

while running:


    dice_art = {
        1: ("┌─────────┐", 
            "│         │", 
            "│    ●    │", 
            "│         │", 
            "└─────────┘"),

        2: ("┌─────────┐", 
            "│  ●      │", 
            "│         │", 
            "│      ●  │",
            "└─────────┘"),

        3: ("┌─────────┐", 
            "│  ●      │", 
            "│    ●    │", 
            "│      ●  │", 
            "└─────────┘"),

        4: ("┌─────────┐", 
            "│  ●   ●  │", 
            "│         │", 
            "│  ●   ●  │", 
            "└─────────┘"),

        5: ("┌─────────┐", 
            "│  ●   ●  │", 
            "│    ●    │", 
            "│  ●   ●  │", 
            "└─────────┘"),

        6: ("┌─────────┐", 
            "│  ● ● ●  │", 
            "│         │", 
            "│  ● ● ●  │",
            "└─────────┘")
    } 


    dice = []
    total = 0
    num_of_dice = int(input("How many dice?: "))

    for die in range(num_of_dice):
        dice.append(random.randint(1,6))

    # for die in range(num_of_dice):
    #  for line in dice_art.get(dice[die]):
    #     print(line)

    for line in range(5):
        for die in dice:
            print(dice_art.get(die)[line], end="")
        print()

    for die in dice:
        total += die


    print(f"total: {total}")

    print(dice)

    while True:
        again = input("Wanna play again? (y/n): ")
        if again == "y":
            break
        elif again == "n":
            running = False
            print("Thank you for a splendid time!")
            break
        else:
            print("Incorrect choice! Choose y or n: ")