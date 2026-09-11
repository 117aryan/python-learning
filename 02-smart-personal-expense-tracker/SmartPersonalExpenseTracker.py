print("========================================")
print("     SMART PERSONAL EXPENSE TRACKER     ")
print("========================================")

name = input("Enter your name: ")
salary = int(input("Enter your salary: "))

expenses = []


def add_expense():
    expense_name = input("Enter expense name: ")
    amount = int(input("Enter amount: "))

    expenses.append([expense_name, amount])

    print("Expense added successfully!")


def view_expenses():
    print("------------ EXPENSES ------------")

    if len(expenses) == 0:
        print("No expenses added yet.")
    else:
        for expense in expenses:
            print(expense[0], "₹",expense[1])


def calculate_total():
    total = 0

    for expense in expenses:
        total = total + expense[1]

    return total


def check_budget():
    total = calculate_total()
    remaining = salary - total

    print("Monthly Income: ₹", salary)
    print("Total Expenses: ₹", total)
    print("Remaining Money: ₹", remaining)

    if remaining >= 0:
        print("Status: You're within your budget.")
    else:
        print("WARNING: You have exceeded your budget!")


while True:

    print("""
---------- MENU ----------

1. Add an expense
2. View expenses
3. Calculate total
4. Check budget
5. Exit
""")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_expense()

    elif choice == 2:
        view_expenses()

    elif choice == 3:
        total = calculate_total()
        print("Total Expenses: ₹", total)

    elif choice == 4:
        check_budget()

    elif choice == 5:
        print("Thank you for using Smart Personal Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")