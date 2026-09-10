print("================================")
print("      PERSONAL EXPENSE APP      ")
print("================================")

user_name = input("Enter your name: ")
monthly_income = int(input("Enter your monthly income: ₹"))

rent = int(input("\nEnter rent: ₹"))
food = int(input("Enter food expenses: ₹"))
transport = int(input("Enter transport expenses: ₹"))
other_expenses = int(input("Enter other expenses: ₹"))

total_expenses = rent+food+transport+other_expenses
remaining_money = monthly_income - total_expenses
income_spent = (100*total_expenses)/monthly_income
daily_allowance = remaining_money/30

print("\n--------------------------------")
print("Monthly Income: ₹", monthly_income)
print("Total Expenses: ₹", total_expenses)
print("Remaining Money: ₹", remaining_money)
print("Income Spent: ", income_spent,"%")
print("Daily Allowance: ₹", daily_allowance,)