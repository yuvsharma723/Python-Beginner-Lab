# Railway Ticket Counter (Python)

A simple **Python console-based railway ticket booking system** that simulates how tickets might be booked at a railway counter. The program collects passenger details, validates inputs, and limits the number of seats available.

## 👨‍💻 Author
**Yuv Sharma**  
GitHub: https://github.com/yuvsharma723

---

## 📌 Project Description
This project is a basic implementation of a **railway ticket booking counter system** using Python classes and loops.

It allows users to:
- Book multiple railway tickets
- Enter passenger details
- Validate user inputs
- Limit the number of seats available
- Continue booking tickets until the user exits

This project is mainly created for **learning and practicing Python programming concepts**.

---

## ⚙️ Features
- 🚆 Ticket booking through a command line interface  
- 👤 Passenger detail input (name, gender, coach number, phone number)  
- 📞 Phone number validation (must be 10 digits)  
- 🚻 Gender validation (male / female / other)  
- 🎟 Maximum seat limit of **10 seats**  
- 🔁 Option to continue booking more tickets  
- ⚠ Error handling for invalid ticket number input  

---

## 🧾 How the Program Works

1. The program asks **how many tickets** the user wants to book.
2. For each ticket, it collects:
   - Name
   - Gender
   - Coach number
   - Phone number
3. The program validates:
   - Gender must be `male`, `female`, or `other`
   - Phone number must be **10 digits**
4. If the total seats reach **10**, booking stops.
5. After booking, the user is asked if they want to **book more tickets**.

---

## 🖥 Example Run
```
how many tickets do you want to book? 2

Enter your name: Yuv
Enter your gender: male
Enter your coach number: B2
Enter your 10-digit phone number: 9876543210
Your ticket has been booked successfully!

Enter your name: Rahul
Enter your gender: male
Enter your coach number: A1
Enter your 10-digit phone number: 9123456789
Your ticket has been booked successfully!

Do you want to book more tickets? (yes/no):
```

## 🧠 Concepts Used
- Python Classes  
- Methods  
- Loops (`while`, `for`)  
- Exception Handling (`try-except`)  
- Input Validation  
- Conditional Statements  

## 🚀 How to Run the Program
1. Clone the repository
```
git clone https://github.com/yuvsharma723/railway-ticket-counter.git
```

2. Navigate to the project folder
```
cd railway-ticket-counter
```

3. Run the Python file
```
python railway_ticket_counter.py
```

## 🔧 Future Improvements
This is a beginner project and I will try my best to improve it over time. In the future I may add better features like improved validation, better seat management, and possibly a graphical interface.
