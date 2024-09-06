"""
Problem statement in another tab.
"""

user_pin = (1234,)
balance = 1000


def check_balance():
    global balance
    print(f"Your Account Balance is: {balance}")


def deposit_money():

    amt = float(input("Enter the amount you want to deposit: "))
    global balance
    balance += amt
    print(f"Cash deposit successful.\n updated balance is {balance}")
    return balance


def withdraw_money():

    amt = float(input("Enter the amount you want to withdraw: "))
    global balance
    if (balance - amt) >= 0:
        balance -= amt
        print(f"Cash withdrawal successful.\nRemaining balance is {balance}")
        return balance
    else:
        print("Insufficient Balance.")
        return balance


print("Welcome to ATM Simulator")

pin = int(input("Please Enter your Pin: "))

if pin == user_pin[0]:
    atm_on = True
else:
    atm_on = False
    print("Incorrect Pin.\n       Thank you for Visiting!...")

while atm_on:
    print("Main Menu:")
    print("1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Exit")
    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        check_balance()
    elif choice == 2:
        deposit_money()
    elif choice == 3:
        withdraw_money()
    elif choice == 4:
        print("Thank you!!...\n    Visit Again...")
        atm_on = False
    else:
        print("Invalid Input.\nPlease Try Again.")




