#=========================================================================================
#TipidTracker: A Simple Budget Manager for Students

#TipidTracker is a Python-based, text-based budget tracker designed to help students
#manage their allowance, expenses, and savings habits. The program makes it easier to
#record daily transactions, track where money is spent, and see summaries over time
#(daily, weekly, monthly, or overall).

#Created by:
#Jassie Shekinah B. Celestino
#Iain Loraine L. Mangawit
#Zane Xavier M. Sanoy

#8-Camia
#=========================================================================================

# Initialize variables and lists
index = 0
total_cost = 0
date_list_allowance = []
date_list_expense = []
allowance_list = []
cost_list = []
item_list = []
remainder = 0
allowance_total = 0
total = 0


#Create function to add allowance
def add_allowance(user_input, allowance_list, index):
    allowance_list.insert(index, user_input)
    print(f"You added {user_input}")


#Create function to add expense
def add_expense(cost, item, cost_list, item_list):
    print()
    item_list.insert(index, item)
    cost_list.insert(index, cost)


#Create function to view all transactions
def view_transactions(allowance_list, item_list, date_list_expense, date_list_allowance, cost_list):
    print()
    print("Allowance added: ")
    print(f"Date: {date_list_allowance}")
    print(f"Allowance: {allowance_list}")
    print()
    print("Expenses: ")
    print(f"Date: {date_list_expense}")
    print(f"Item: {item_list}")
    print(f"Cost: {cost_list}")
    print()


#Create function to check the summary of all transactions
def add_summary(total, allowance_total, remainder):
    print()
    print(f"Allowance total: {allowance_total}")
    print()
    print(f"Expense total: {total}")
    print()

    remainder = allowance_total - total

    print(f"Remainder: {remainder}")
    print()


# While loop to keep user in the program
while 1 != 2:

    #Main menu
    print("="*50, " MAIN MENU ", "="*50)
    print("1. Add allowance")
    print("2. Add expense")
    print("3. View transactions")
    print("4. View summary")

    print("Enter '0' to exit program.")

    print("=" * 113)

    #Ask for user input
    user_input = int(input("Enter your choice: "))
    print()

    #Create if statements checking possibilities
    if user_input == 1:

        user_input = float(input("Add allowance (ex. 50 php add): "))
        if user_input == 0 or user_input<0:
            print("Invalid inputs will not be recorded.")
            print()
            continue

        allowance_total += user_input

        from datetime import date

        current_date = date.today()
        date = current_date.strftime("%Y-%m-%d")
        date_list_allowance.insert(index, date)

        add_allowance(user_input, allowance_list, index)

    elif user_input == 2:

        cost = float(input("Money spent: "))

        if cost == 0:
            print("An input of 0 will not be recorded.")
            print()
            continue

        total += cost

        if allowance_total - total < 0:
            total -= cost
            print("You spent too much!")
            continue

        item = str(input("What item was the money spent on? "))

        from datetime import date

        current_date = date.today()
        date = current_date.strftime("%Y-%m-%d")
        date_list_expense.insert(index, date)

        add_expense(cost, item, cost_list, item_list)

    elif user_input == 3:
        view_transactions(allowance_list, item_list, date_list_expense, date_list_allowance, cost_list)

    elif user_input == 4:
        add_summary(total, allowance_total, remainder)

    elif user_input == 0:
        break

    #Invalid user input
    else:
        print("Invalid input.")
        print()
    print()

    return_menu = str(input("Would you like to go back to the main menu? (Yes/No) "))

    if return_menu.lower() == "Yes":
        continue
    else:
        break

#End program
print("="*113)
print("\nThank you for using our program!\n")
print("="*113)
