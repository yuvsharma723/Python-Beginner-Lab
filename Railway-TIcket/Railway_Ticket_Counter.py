class railway_ticket_counter:
    name = "rail"
    gender = ""
    coach_no = 0
    phone_no = "1234567890"
    seat = 0
    def book_ticket(self):
        if self.seat >= 10:
            print("Sorry, all tickets are booked.")
            return
        else:
            name = input("Enter your name: ")
            i=0
            while i==0:
                gender = input("Enter your gender: ")
                if gender.lower() == "male" or gender.lower() == "female " or gender.lower() == "other":
                    i=1
                else:
                    print("Please enter a valid gender (male, female, or other).")
                    i=0
            coach_no = (input("Enter your coach number: "))
            
            k=0
            while k==0:
                phone_no = input("Enter your 10-digit phone number: ")
                if len(phone_no) == 10:
                    k=1
                else:
                    print("Please enter a valid 10-digit phone number.")
                    k=0
            print ("Your ticket has been booked successfully!")
            self.seat += 1
u = 0
while u==0:
    ticket = railway_ticket_counter()
    try:
        ticket_require = int(input("how many tickets do you want to book? "))
        for i in range(1,ticket_require+1):
            ticket.book_ticket()
    except :
        print("Please enter a valid number of tickets to book.")
    ask = input("Do you want to book more tickets? (yes/no): ")
    if ask.lower() == "yes":
        u=0
    else:     
        u=1
        print("Thank you for using the railway ticket counter. Have a nice day!")
