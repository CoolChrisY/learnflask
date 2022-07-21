import random
Password=random.randint(1, 20)
Answer= eval(input("What is the password?"))
while Answer>Password or Answer<Password:
    Answer= eval(input("What is the password?"))
    if Answer==Password:
        print("you win!")

    else:
        print("try again.")