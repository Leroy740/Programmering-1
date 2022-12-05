import random
user_score=0
computer_score=0
user_name=input("vad heter du? ")


while user_score <3 and computer_score <3:
    computer = random.choice(["rock", "paper", "scissors"])

    user = input("rock, paper or scissors? ")
    print(f"Du valde {user} och datorn valde {computer}")
    if user == computer:
        print("Draw inga poäng. ")

    elif user == "rock" and computer == "scissors":
        print(f"{user_name} fick ett poäng ")
        user_score = user_score+1

    elif user == "paper" and computer == "rock":
        print(f"{user_name} fick ett poäng ")
        user_score = user_score+1

    elif user == "scissors" and computer == "paper":
        print(f"{user_name} fick ett poäng ")
        user_score = user_score+1


    elif user == "paper" and computer == "scissors":
        print(f"{computer} fick ett poäng ")
        computer_score = computer_score+1 

    elif user == "scissors" and computer == "rock":
        print(f"{computer} fick ett poäng ")
        computer_score = computer_score+1

    elif user == "rock" and computer == "paper":
        print(f"{computer} fick ett poäng ")
        computer_score = computer_score+1


# Implement the if statements that prints who wins