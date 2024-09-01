import random

user_wins=0
computer_wins=0
options=["rock","paper","scissor"]

while True:
    user_input= input("Enter Rock/Paper/Scissor or Q to quit:").lower()
    if user_input=="q":
        break

    if user_input not in options:
        # print("wrong input, try again!!")
        continue

    random_number= random.randint(0,2)
    # rock:0 , paper:1 , scissor:2
    computer_pick = options[random_number]
    print("computer picked",computer_pick)

    if user_input== "rock" and computer_pick == "scissor":
        print("congrats, you won")
        user_wins+=1

    elif user_input== "paper" and computer_pick == "rock":
        print("congrats, you won")
        user_wins+=1

    elif user_input== "scissor" and computer_pick == "paper":
        print("congrats, you won")
        user_wins+=1

    elif user_input == computer_pick:
        print("oops its a tie!!")

    else:
        print("you lost")
        computer_wins+=1

print("You won", user_wins, "times.")
print("Computer won", computer_wins, "times.")
print("Goodbye!")
    

