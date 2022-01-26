import random
concent=input("Welcome!Do you wanna play, Rock, Paper,Scissors..?(Yes/No):")
concent=concent.lower()
if concent=="yes" or concent=="y":
    score=0
    tie=0
    while True:
        possible_actions = ["rock", "paper", "scissors"]
        computer_guess = random.choice(possible_actions)
        print(f"compGuess:{computer_guess}")
        attempt=input("Come on Grace, Enter your try,(choose between rock,paper,scissors):")
        attempt.lower()
        if attempt=="rock":
            if computer_guess=="rock":
                print(f"it\'s a tie!")
                tie+=1
                print("Tie:{}".format(tie))
            elif computer_guess=="paper":
                print("You lose!Paper covers Rock")
            elif computer_guess=="Scissors":
                print("Hurray! Rock smashes scissors")
                score+=1
                print("Score {}".format(score))
            else:
                print("Press Enter to continue")
        elif attempt=="paper":
            if computer_guess=="rock":
                print("Hurray!--->paper covers rock. You won!")
                score+=1
                print("Score {}".format(score))
            elif computer_guess=="paper":
                print("It\'s a tie!")
                tie+=1
                print("Tie: {}".format(tie))
            elif computer_guess=="scissors":
                print("Oops!--->scissors cut paper. You lose!")
            else:
                print("---."*56)
        elif attempt=="scissors":
            if computer_guess=="rock":
                print("Oops!---> rock crushes scissors.You lose!")
            elif computer_guess=="paper":
                print("Hurray!---> scissors cut paper. You won!")
                score+=1
                print("Score {}".format(score))
            elif computer_guess=="scissors":
                tie+=1
                print("It\'s a tie.")
            else:
                print("+"*30)
        else:
            print("Invalid Entry, please Try again!!!")
elif concent=="no" or concent=="n":
    print("Exited Successfully.")

else:
    print("Invalid Entry!!!")
    exit()








