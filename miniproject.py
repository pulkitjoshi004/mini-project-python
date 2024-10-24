import random
'''
1 for snake
-1 for water
0 for gun

'''

computer = random.choice([1,2,3])
youstr= input("Enter your choice: ")

youdict= {"s":1,"w":-1,"g":0}
reversdict={1:"rock",2:"paper",3:"scissor"}

you=youdict[youstr]

#by now we have 2 numbers (variables), you and computer

print(f"you chose{reversdict[you]}\n computer choice{reversdict[computer]}")

if(computer==you):
    print("its a draw")
else:
    if(computer==-1 and you==1):
        print("you win!")
    elif(computer==-1 and you==0):
        print("you loose!")
    elif(computer==1 and you==-1):
        print("you loose!")
    elif(computer==1 and you==0):
        print("you win!")
    elif(computer==0 and you==-1):
        print("you win!")
    elif(computer==0 and you==1):
        print("you loose!")
    else:
        print("something went wrong")
