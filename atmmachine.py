account_balance = 5000
atm_pin = "4444"

def validate_pin():
    for attempt in range(3):
        entered_pin = input("Enter 4 digit pin: ")
        if entered_pin == atm_pin:
            print("login Sucessfull----")
            return True
        else:
            print("Incorrect pin!! Please try again!!!!")
    print("Too many attempts. Exiting........")
    return False

# Function to check balance

def check_balance():
    print(f"Your current account balance is {account_balance}")


# Function to deposit money

def deposit_money():
    global account_balance
    try:
        amount = float(input("Enter the amount to deposit:"))
        if amount > 0:
            account_balance += amount
            print (f"₹{amount} deposited sucessfully!!!")
            check_balance()
        else:
            print("Invalid amount Deposit Failed.")
    except ValueError:
        print("Invalid input ! Try with numeric value")


# Fucntion to withdraw money

def withdraw_money():
    global account_balance
    try:
        amount = float(input("Enter the amount u want to withdraw: "))
        if 0 < amount <= account_balance:
            account_balance -= amount
            print (f"₹{amount} withdrawn sucessfully")
            check_balance()
        elif amount > account_balance:
            print("Insuffecient funds!!")
        else:
            print("Invalid amount. Withdrwal Failed.")
    except ValueError:
        print("Invalid input ! Please try again with numeric value")

def main_menu():
    while True:
        print("\n----ATM MENU----")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Select an option:")
        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
             print("Thank you for using the ATM. Goodbye!")
             break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    print("Welcome to ATM!")
    if validate_pin():
        main_menu()




