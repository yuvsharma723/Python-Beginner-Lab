i=0
while(i<1):
    try:
        n = int(input("enter no. you want to check wheather it is prime or not: "))
        if(n==1 or n==0):
            print("your no. prime neither composite")
        for i in range(2,n):
            if(n%i==0):
                print("your no. is not prime")
                break
        else:
            print("your no. is prime")
        print("thank you \n if you want to check another no. (enter yes) or write nothing")
        k= input("please enter here: ")
        if("yes" in k.lower()):
            i=0
        else:
            print("thank you")
            i+=1
    except:
        print("please enter valid no.")