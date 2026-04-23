# =========================================================================================
# TipidTracker: A Simple Budget Manager for Students

# TipidTracker is a Python-based, text-based budget tracker designed to help students
# manage their allowance, expenses, and savings habits. The program makes it easier to
# record daily transactions, track where money is spent, and see summaries over time
# (daily, weekly, monthly, or overall).

# Created by:
# Jassie Shekinah B. Celestino
# Iain Loraine L. Mangawit
# Zane Xavier M. Sanoy

# 8-Camia
# =========================================================================================

# Import needed libraries
import json
import time
from datetime import datetime

# Reading from the file
filename = 'tipidtracker_data.json'
with open(filename, 'r') as file:
    # Load the JSON data from the file
    data = json.load(file)

# Initialize all needed variables
allowance = 0
date_list = []
expense_list = []
total_expense_added = 0
total_allowance_added = 0
category = ["food", "school", "leisure", "health", "transportation", "personal care"]

# Message for the user to understand the program
print("Hello user!")
print("\nWelcome to TipidTracker! this is a Python-based, text-based budget tracker designed to help students"
      "\nmanage their allowance, expenses, and savings habits. The program makes it easier to"
      "\nrecord daily transactions, track where money is spent, and see summaries over time.")
print("\nEnjoy using this program!")
time.sleep(2)

# Create a loop that doesn't end until the user wants to end it
while 1 == 1:

    # Create main menu
    print("=" * 50, " MAIN MENU ", "=" * 50)
    print("1. Add allowance")
    print("2. Add expense")
    print("3. View transactions")
    print("4. View summary")

    print("Enter '0' to exit program.")

    print("=" * 113)

    # This asks the user to input their choice
    while True:
        try:
            choice = int(input("\nEnter your choice: "))
            print()
            break
        except ValueError:
            print("Please enter a valid number.")

    if choice == 1:
        # Allows the user to input their allowance
        add_allowance = input("Add allowance (ex. 50.00): ")

        while True:
            try:
                value = float(add_allowance)
                if value.is_integer():
                    if value < 0:
                        print("Please enter a valid number.")
                        add_allowance = float(input("Add allowance: "))
                    else:
                        break
                else:
                    if value < 0:
                        print("Please enter a valid number.")
                        add_allowance = float(input("Add allowance: "))
                    else:
                        break
            except ValueError:
                print("Please enter a valid number.")
                add_allowance = input("Add allowance (ex. 50.00): ")

        total_allowance_added += float(add_allowance)
        allowance += float(add_allowance)

        # Add current date
        current_date = datetime.now()
        format_date = current_date.strftime("%y:%m:%d")
        formatted_date = f"Added_allowance at {format_date}."
        date_list.append(formatted_date)

        # Editing the JSON file
        with open(filename, 'r') as file:
            data = json.load(file)
            # Put added allowance in the JSON file
            data["Allowance_added"] += float(add_allowance)
            print("Thank you! Remember to spend your money wisely.")

    if choice == 2:
        # Allows the user to input their expense
        add_expense = input("Add expense: ")

        # Warning the user to not spend too much money
        if add_expense > allowance:
            print("Oops! You're spending too much!")

        try:
            value = float(add_expense)
            if value.is_integer():
                if value < 0:
                    print("Please enter a valid number.")
                    add_expense = float(input("Add expense: "))
                else:
                    break
            else:
                if value < 0:
                    print("Please enter a valid number.")
                    add_expense = input("Add expense: ")
                else:
                    break
        except ValueError:
            print("Please enter a valid number.")
            add_expense = float(input("Add expense: "))

       total_expense_added += float(add_expense)
        allowance -= float(add_expense)
        expense_list.append(add_expense)

        # Add category and description (optional)
        category_choice = input("What category were they spent on? (food, school, leisure, health, transportation, personal care): ")
        if category_choice not in category:
            print("Please enter a valid category.")
        else:
            category.append(category_choice)

        descrip_choice = input("Would you like to put a description? (Yes/No) ")
        if descrip_choice.lower() == "yes":
            description = input("Add description: ")
        else:
            pass

        if descrip_choice.lower() == "yes":
            formatted_date = f"Added_expense at {format_date} Category: {category_choice} Description: {description}."
        else:
            formatted_date = f"Added_expense at {format_date} Category: {category_choice}."
        date_list.append(formatted_date)

        # Add current date
        current_date = datetime.now()
        formatted_date = current_date.strftime("%y:%m:%d")
        
        if descrip_choice.lower() == "yes":
            formatted_date = f"Added_expense at {formatted_date} Category: {category_choice} Description: {description}."
        else:
            formatted_date = f"Added_expense at {formatted_date} Category: {category_choice}."
        date_list.append(formatted_date)

        # Editing the JSON file
        with open(filename, 'r') as file:
            data = json.load(file)
            # Put added expense in the JSON file
            data["Expenses_added"] += float(add_expense)

        # Editing the JSON file
        with open(filename, 'r') as file:
            data = json.load(file)
            # Put data of the variable expense list in the expense list in the JSON file
            data["Expenses_list"] += expense_list

    if choice == 3:
        # Prints the transaction history of the user.
            if data["Dates"] == 0:
                print("No transaction recorded.")
            else:
                print("Please enter a valid choice.")
                print("Enter 'F' to show full transaction history.")
                print("Enter 'A' to show allowance history only.")
                print("Enter 'E' to show expense history only.")
                time.sleep(2)

                transaction_choice = input("Enter choice: ")

                while transaction_choice.lower() not in ["f", "a", "e"]:
                    print("Please enter a valid choice.")
                    transaction_choice = input("Enter choice: ")

                if transaction_choice.lower() == "f":
                    for i in date_list:
                        print(i)
                elif transaction_choice.lower() == "a":
                    for i in date_list:
                        if "Added allowance" in i:
                            print(i)
                elif transaction_choice.lower() == "e":
                    for i in date_list:
                        if "Added expense" in i:
                            print(i)

    if choice == 4:
        allowance_total = data[("Allowance_added")]
        total = data["Expenses_added"]
        remainder = allowance_total - total

        print(f"Total Allowance: {data["allowance_total"]}")
        print(f"Total Expenses: {total}")
        print(f"Remaining Balance: {remainder}")

    # Ask the user if they want to continue the program or not
    return_menu = str(input("\nWould you like to go back to the main menu? (Yes/No): "))
    while return_menu.lower() not in ["no", "yes"]:
        print("Please enter a valid choice.")
        return_menu = str(input("\nWould you like to go back to the main menu? (Yes/No): "))

    if return_menu.lower() == "yes":
        continue
    else:
        # End program
        print("Thank you for using this program!")
        break

