import random
choices = ("rock", "paper", "scissors")
playerchoice = None
while True:
    while playerchoice not in choices:
        playerchoice = input("Enter a choice (paper,rock,scissors) : ").lower()
    print(f"Player : {playerchoice}")
    computerchoice = random.choice(choices)
    print(f"Computer : {computerchoice}")
    if playerchoice == computerchoice:
        print("No one")
    elif playerchoice == "rock" and computerchoice == "scissors":
        print("You win")
    elif playerchoice == "paper" and computerchoice == "rock":
        print("You win")
    elif playerchoice == "scissors" and computerchoice == "paper":
        print("You win")
    else:
        print("You lose")
    yorn = input("Play again (y/n): ").lower()
    if yorn == "y":
        continue
    else:
        break
print("thank you for playing")
