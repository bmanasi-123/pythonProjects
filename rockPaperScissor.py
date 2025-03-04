#rockPaperScissor
import random

rock = "rock"
paper = "paper"
scissor = "scissor"
choices=[rock,paper,scissor]
# print(choices)
start = True
while start:
    button = input("Type 'Play' to start the game | Type 'Stop' to stop the game \n")
    if button.lower() == 'stop':
        print('Thanks for playing')
        start = False
        break
    userChoice = int(input("What do you choose ? 0 for Rock , 1 for Paper , 2 for Scissor \n"))

    if userChoice > 2 or userChoice < 0:
        print("Enter a valid numeric to choose.")
    else:
        print("Your choice:\n"+choices[userChoice])

        computerChoice = random.randint(0, 2)
        print("Computer choice:\n" + choices[computerChoice])

        if userChoice == computerChoice:
            print("It's a Tie!")
        elif userChoice>0 and userChoice<computerChoice:
            print("You Lose!")
        elif userChoice == 2 and computerChoice == 0:
            print("You Lose!")
        else:
            print("You Win!")

