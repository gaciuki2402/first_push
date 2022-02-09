import random
class people_going_for_charity_work():
    def List(self):
        self.concent=input("Do you want to volunteer?Yes/No")
        concent=self.concent.lower()
        self.volunteers=input("Enter your name:").title()
        names=["John","Mary","Grace"]#,"Davie","Irene","Jack","Belta","John"]
        #the principal needs only four names
        vol=[]
        for i in range(len(names)):
            principal_pick = random.choice(names)
            vol.append(principal_pick)
        vol=set(vol)
        print(vol)
        if self.volunteers in vol:
            print("You were selected to join the group")
        else:
            print("Ooops! You were not selected to join the group")
    def Details(self):
        for students in self.volunteers:
            details={

            }
            fName=input("Enter First name:")
            lname=input("Enter surname:")
            adm=input("Enter Admission Number:")
            age=input("Enter Age:")
            phone_number=input("Enter contact:")
            email=input("Enter email:")
            details["First name"]=fName
            details["Surname"]=lname
            details["Admission number"]=adm
            details["Age"]=age
            details["Contact"]=phone_number
            details["Email"]=email
            print(details)





c1=people_going_for_charity_work()
c1.List()
c1.Details()
