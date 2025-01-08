#  first we will know what will be in expense tracker
# Expense tracker:
# Add expenses
# view expenses 
# calculate total expenses
# save to file

expenses = []
def show_menu():
    print("\nExpense Tracker ")
    print("1. Add expenses")
    print("2. View expenses")
    print("3. Calculate expenses")
    print("4. Save expenses to file")
    print("5. Load expenses from file")
    print("6. Exit")

# now we will add all functionality of menu

def add_expenses():
    description = input("Enter the description:")
    amount = float(input("Enter the amount:"))
    date  = input("Enter the data (DD-MM-YYYY)")
    expenses.append({"description":description, "amount":amount, "date":date})
    print("Expense added sucessfully!!")

def view_expenses():
    if not expenses:
        print("No expenses recorded")
    else:
        print("\nExpenses:")
        for i, expense in enumerate(expenses,1):
            print(f"{i}. {expense['date']} - {expense['description']}: ${expense['amount']:.2f}")

def calculate_expenses():
    total = sum(expense['amount'] for expense in expenses)
    print(f"\nTotal expenses: ${total:.2f}")

def save_to_file():
    filename= input("Enter the filename to save to:")
    try:
        with open(filename, 'w') as  file:
            for expense in expenses:
                file.write(f"{expense['date']},{expense['description']},{expense['amount']}\n")
        print("Expenses added sucessfully-------//")
    except Exception as e:
        print(f"Error saving to file: {e}")

def load_from_file():
    filename = input("Enter the filename to load from")
    try:
        with open(filename  , 'r') as file:
            for line in file:
                date, description, amount = line.strip().split(',')
                expenses.append({"date": date, "description": description, "amount": float(amount)})
        print("Expenses loaded sucessfully--------//")
    except Exception as e:
        print(f"Error loading from file: {e}")

def exit():
    print("Good-Bye 👋")
    exit()


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-6) :")
        
        if choice == '1':
            add_expenses()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            calculate_expenses()
        elif choice == '4':
            save_to_file()
        elif choice == '5':
            load_from_file()
        elif choice == '6':
            exit()
        else:
            ("Invalid Input !!!")
if __name__ == "__main__":
    main()
