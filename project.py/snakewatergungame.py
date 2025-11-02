import random

'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([0,-1,1])
youstr= input("chose s for snake, w for water, g for gun: ")
youDict= {"s":1, "w":-1, "g":0}
reverseDict= {1:"snake", -1:"water", 0:"gun"}

you= youDict[youstr]
print(f"You chose {reverseDict[you]}\n Computer chose {reverseDict[computer]}")

if(computer==you):
    print("It's a DRAW")

else:
    if(computer==-1 and you==1):
        print("YOU WIN!")
    elif(computer==-1 and you==0):
        print("YOU LOSE!")
    elif(computer==1 and you==--1):
        print("YOU LOSE!")
    elif(computer==1 and you==0):
        print("YOU WIN!")
    elif(computer==0 and you==-1):
        print("YOU WIN!")
    elif(computer==0 and you==1):
        print("YOU LOSE!")
    else:
        print("SOMETHING WENT WRONG")