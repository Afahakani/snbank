import random
import os
from datetime import datetime


# create a session for successful login and record the date and time
def create_session():
    f = open("session.txt", "w")
    f.write("User Successfully logged in at: " + datetime.now().strftime("%Y%m%d - %H%M%S"))
    f.close()


# create customer accounts
def new_account():
    account_details = []
    Account_Name = input("\nName of Account: ")
    Opening_Balance = input("Opening Balance: ")
    Account_Type = input("Type of Account: ")
    Account_Email = input("Account Email: ")
    account_number = str(random.randrange(10**9, 10**10))

    str1 = " \nAccount Number: " + account_number
    str2 = " \nAccount Name: " + Account_Name
    str3 = " \nOpening Balance: " + Opening_Balance
    str4 = " \nAccount Type: " + Account_Type
    str5 = " \nAccount Email: " + Account_Email
    str6 = " \n**********"

    account_details.extend((str1, str2, str3, str4, str5, str6))
    newCustomer = open("customer.txt", "a")
    newCustomer.writelines(account_details)
    newCustomer.close()
    print("Account Details Entered Successfully!")
    print("Account Number is: ", account_number)
    task_options()


# checks customer's account using account number
def check_account():
    accountNumber = input("Enter Account Number: ")
    custFile = open("customer.txt", "r").read()
    StrAccNum = "Account Number: " + accountNumber
    if StrAccNum in custFile:
        firstLine = custFile.find(StrAccNum)
        custDetails = custFile[firstLine:]
        lastLine = custDetails.find("**********")
        custDetails = custDetails[:lastLine]
        print("\nThe Customer Details are:\n" + custDetails)
    else:
        print("Customer Details Not Found")
    task_options()


# Login for staff already registered
def staff_login():
    userName = input("\nYour UserName: ").lower()
    password = input("Your Password: ").lower()
    string = "User Name: " + userName + " Password: " + password
    staffFile = open("staff.txt", "r").read()
    if string in staffFile:
        create_session()
        task_options()
    else:
        print("Your Username and password are incorrect. Try again!")
        staff_login()


# Showing the different tasks a staff can perform on the app
def task_options():
    print("""
1. Create New Bank Account
2. Check Account Details
3. Logout
""")
    taskSelect = int(input("Select your Task Options (Type 1, 2, or 3): "))
    if taskSelect == 1:
        new_account()
    elif taskSelect == 2:
        check_account()
    else:
        os.remove("session.txt")
        initialStart()


# prompts staff to use the app
def initialStart():
    print("""
1. Staff Login
2. Close App """)
    staffActions = int(input("\nType 1 to Login or 2 to Close the App: "))
    if staffActions == 1:
        staff_login()
    elif staffActions == 2:
        exit(0)


# creates text files for staff and customer
def createTextFiles():
    staffFile = open("staff.txt", "w")
    staff_details = ["User Name: smonica Password: monicasimpsons ", "\nEmail: m.simpsons@gmail.com ", "\nFull Name: Monica Simpsons ",
            "\n\nUser Name: dpatrick Password: patrickdywer ", "\nEmail: p.dywer@gmail.com", "\nFull Name: Patrick Dywer "]
    staffFile.writelines(staff_details)
    staffFile.close()

    customerFile = open("customer.txt", "w")
    customerFile.close()


# calls the functions for execution of the ap
createTextFiles()
print("This is a Basic Banking System App")
initialStart()
