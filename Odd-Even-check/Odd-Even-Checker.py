i=0
while i==0:
    try:
        number = int(input("Enter a number: "))
        print("The number is", "even" if number % 2 == 0 else "odd")
    except:
        print("Invalid input. Please enter an integer.")
    done = input("Do you want to check another number? (yes/no): ")
    if done.lower() == "yes":
        i=0
    else:
        print("Thank you for using the Odd-Even Checker. Goodbye!")
        i=1
