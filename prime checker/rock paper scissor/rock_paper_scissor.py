import random
k=0 
while k < 1:
    print("welcome to rock paper scissor game") 
    try:
        no= int(input("how many times you want to play : "))
    except :
        print("please enter a valid number")
        no= int(input("how many times you want to play : "))
    urwin=0 
    computerwin=0
    i=0
    while i < no:
        
        a= input("please choose from rock , paper and scissor(choosing something else, result in lose) : " )
        b= random.choice(["rock", "paper", "scissor"])
        if a.lower() == b:
            print("tie")
        elif a.lower() == "rock" and b == "scissor":
            print("you win")
            urwin+=1            
        elif a.lower() == "paper" and b == "rock":
            print("you win")
            urwin+=1
        elif a.lower() == "scissor" and b == "paper":
            print("you win")
            urwin+=1
        else:
            print("you lose")
            computerwin+=1
        print("computer choose : " + b)
        print("your score : " + str(urwin))
        print("computer score : " + str(computerwin))
        i+=1
    if urwin > computerwin:
        print("congratulations you win the game")
    elif computerwin > urwin:
        print("sorry you lose the game")
    else:
        print("the game is tie")
    want= input("do you want to continue (y/n) : ")
    if want.lower() == "y":
        i=0
    else:
        print("thank you for playing")
        break