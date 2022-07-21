import random
Answer=input("Do you want to play?")
while Answer==("yes") or Answer==("yes"):
    numbers=1, 2, 3, 4, 5, 6, 7, 8, 9
    random.shuffle(numbers)
    numbers2=1, 2, 3, 4, 5, 6, 7, 8, 9
    random.shuffle(numbers2)
    Sum=input("%s+%s="%numbers, numbers2)
    Added=numbers+numbers2
    if Sum=Added:
        print ("Correct!😁")
    Answer=input("Do you want to play again?")
    
