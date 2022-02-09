import random
concent=input("Are you ready for the challenge?(Y/N)")
concent=concent.lower()
if concent=="Y" or concent=="Yes":
    points=0
    while True:
        possible_questions=["1:The tallest animal","2.Animal found in the northern pole","3.Thee fastest animal"]
        print(possible_questions)
        possible_answers=["giraffe","polar_bear","cheetah"]
        Answers=random.choice(possible_answers)
        print(Answers)
        First_Question="Which is the tallest."
        print(First_Question)
        my_answer=input("Welcome to today's challenge!:(choose between giraffe,polar_bear,cheetah):")
        if my_answer=="cheetah":
            if Answers=="giraffe":
                print(f"Wrong Answer.")
                points+=0
                print("Points:{}".format(points))
            elif Answers=="polar_bear":
                print(f"Wrong Answer!")
                points+=0
                print("Points:{}".format(points))
            elif Answers=="cheetah":
                print(f"Correct Answer.Congratulation!")
                points+=10
                print("Points:{}".format(points))
            print(f"Attempt:{Answers}")
        elif my_answer=="giraffe":
            Second_Question = "Which animal is found in the northern pole?"
            print(Second_Question)
            if Answers=="polar_bear":
                print(f"Wrong Answer!")
                points+=0
            elif Answers=="giraffe":
                print(f"Correct Answer")
                points+=10
                print("Points:{}".format(points))

            elif Answers=="cheetah":
                print(f"Wrong answer")
                points+=0
        elif my_answer=="Polar_bear":
            Third_Question = "Which is the fastest animal."
            print(Third_Question)
            if Answers=="giraffe":
                print(f"Wrong Answer!")
                points+=0
            elif Answers=="polar_bear":
                print(f"Correct answer.Congratulation!!!")
                points+=10
            elif Answers=="cheetah":
                print(f"Wrong Answer!!!")
                points+=0
                print("Points:{}".format)

        else:
            print("INVALID ANSWERS!!!")
elif concent=="No" or concent=="N":
    print("Exit")


