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
    choice = int(input("\nEnter your choice: "))
    print()

    if choice == 1:
        # Allows the user to input their allowance
        add_allowance = float(input("Add allowance (ex. 50 php add): "))

        if add_allowance<0:
            print("Please enter a valid number.")
            continue
        elif type(add_allowance) is not float:
            print("Please enter a valid number.")
            continue

        total_allowance_added += add_allowance
        allowance += add_allowance

        # Add current date
        current_date = datetime.now()
        format_date = current_date.strftime("%y:%m:%d")
        formatted_date = f"Added_allowance at {format_date}."
        date_list.append(formatted_date)

        # Editing the JSON file
        with open(filename, 'r') as file:
            data = json.load(file)
            # Put added allowance in the JSON file
            data["Allowance_added"] += add_allowance
            print("Thank you! Remember to spend your money wisely.")

    elif choice == 2:
        # Allows the user to input their expense
        add_expense = float(input("Add expense: "))

        # Warning the user to not spend too much money
        if add_expense > allowance:
            print("Oops! You're spending too much!")

        if add_expense<0:
            print("Please enter a valid expense.")
            continue
        elif type(add_expense) is not float:
            print("Please enter a valid expense.")
            continue

        total_expense_added += add_expense

        allowance -= add_expense
        expense_list.append(add_expense)

        # Add category and description (optional)
        category_choice = input(
            "What category were they spent on? (food, school supplies, leisure, health, transportation, personal care): ")
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
            data["Expenses_added"] += add_expense

        # Editing the JSON file
        with open(filename, 'r') as file:
            data = json.load(file)
            # Put data of the variable expense list in the expense list in the JSON file
            data["Expenses_list"] += expense_list

    elif choice == 3:
        # Prints the transanction history of the user.

        if len(data["Expenses_list"]) == 0:
            print("No transanction recorded.")

        else:

            for i in range(len(data["Expenses_list"])):
                print(f"Data: {data["Dates"][i]}")
                print(f"Item: {data["Expenses_list"][i]}")

    elif choice == 4:

        allowance_total = data[("Allowance_added")]
        total = data["Expenses_added"]
        remainder = allowance_total - total

        print(f"Total Allowance: {data["allowance_total"]}")
        print(f"Total Expenses: {total}")
        print(f"Remaining Balance: {remainder}")

    # Ask the user if they want to continue the program or not
    return_menu = str(input("\nWould you like to go back to the main menu? (Yes/No): "))

    if return_menu.lower() == "yes":
        continue
    else:
        # End program
        print("Thank you for using this program!")
        break
