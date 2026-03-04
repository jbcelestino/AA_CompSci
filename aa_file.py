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
import json

filename = 'tipidtracker_data.json'

with open(filename, 'r') as file:
    data = json.load(file)

index = 0
allowance = 0
date_list = []
money_left = 0
expense_list = []
total_expense_added = 0
total_allowance_added = 0
while 1 == 1:
    print("=" * 50, " MAIN MENU ", "=" * 50)
    print("1. Add allowance")
    print("2. Add expense")
    print("3. View transactions")
    print("4. View summary")

    print("Enter '0' to exit program.")

    print("=" * 113)

    # This asks the user to input their choice
    user_input = int(input("Enter your choice: "))
    print()

    if user_input == 1:

        user_input2 = float(input("Add allowance (ex. 50 php add): "))

        total_allowance_added += user_input2
        allowance += user_input2
        money_left += user_input2

        with open(filename, 'r') as file:
            data = json.load(file)
            for x in data:
                x['Allowance_added'] = total_allowance_added

            for x in file:
                print(x)

    elif user_input == 2:
        user_input2 = float(input(""))

        user_input3 = str(input(""))

        if user_input > allowance:
            print("You are now in debt.")

        total_expense_added += user_input2

        allowance -= user_input
        expense_list.append(user_input3)

        with open(filename, 'r') as file:
            data = json.load(file)
            for x in data:
                x['Expenses_added'] = total_expense_added

        with open(filename, 'r') as file:
            data = json.load(file)
            for x in data:
                x['Expenses_list'] = expense_list
