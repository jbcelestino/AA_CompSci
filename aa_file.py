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

#==========================
#Function: Add Allowance
#==========================
def add_allowance(user_input, allowance_list, index):
    allowance_list.insert(index, user_input)
    print(f"You added {user_input}")

#==========================
#Function: Add Expense
#==========================
def add_expense(cost, item, cost_list, item_list):
    print()
    item_list.insert(index, item)
    cost_list.insert(index, cost)

#=======================================
#Function: View All Transanctions
#=======================================
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

#=======================================
#Function: Summary of All Transanctions
#=======================================
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

    #This asks the user to input their choice
    user_input = int(input("Enter your choice: "))
    print()

    #If the user inputs "1" as their choice, the program will ask the user how much money do they want to add into their allowance.
    if user_input == 1:

        user_input = float(input("Add allowance (ex. 50 php add): "))
        #If the user's input is less than or equal to 0, the input will not be recorded and then bring you back to the main menu.
        if user_input == 0 or user_input<0:
            print("Invalid inputs will not be recorded.")
            print()
            continue

        #This will add the inputted amount into the total allowance.
        allowance_total += user_input

        #This tells the date that the allowance added.
        from datetime import date
        
        current_date = date.today()
        date = current_date.strftime("%Y-%m-%d")
        date_list_allowance.insert(index, date)

        add_allowance(user_input, allowance_list, index)

    #If the user inputs "2" as their choice, the program will ask the user how much money did they spend.
    elif user_input == 2:

        cost = float(input("Money spent: "))
    #If the user's input is equal to 0, the input will not be recorded and then bring you back to the main menu.
        if cost == 0:
            print("An input of 0 will not be recorded.")
            print()
            continue

        #This adds the money you spent to the total money you spent.
        total += cost

        #If the total allowance minus the total money spent is less than 0, the program will tell them that they spent too much.
        if allowance_total - total < 0:
            total -= cost
            print("You spent too much!")
            continue

        #The program asks what the user spent their money on
        item = str(input("What item was the money spent on? "))

        #This tells the date of when the money spent.
        from datetime import date

        current_date = date.today()
        date = current_date.strftime("%Y-%m-%d")
        date_list_expense.insert(index, date)

        add_expense(cost, item, cost_list, item_list)
        
    #If the user inputs "3" as their choice, then it will print all the transanctions
    elif user_input == 3:
        view_transactions(allowance_list, item_list, date_list_expense, date_list_allowance, cost_list)
        
    #If the user inputs "4" as their choice, the program will print the summary of all transanctions.
    elif user_input == 4:
        add_summary(total, allowance_total, remainder)

    #If the user inputs "0" as their choice, the program will break/end.
    elif user_input == 0:
        break

    #If the user inputs non of the choices, the program will tell them that their input is invalid, and then ask them if they woulf like to go back to the main menu.
    #Invalid user input    
    else:
        print("Invalid input.")
        print()
    print()

    return_menu = str(input("Would you like to go back to the main menu? (Yes/No) "))

    #Used to validate yes/no
    while checker==0:
        if return_menu.lower() == "yes":
            checker+=1
        elif return_menu.lower() == "no":
            checker+=1
        else:
            print("Invalid input.")
            print("="*113)
            return_menu = str(input("Would you like to go back to the main menu? (Yes/No) "))

    if return_menu.lower() == "yes":
        continue
    else:
        break

#End program
print("="*113)
print("\nThank you for using our program!\n")
print("="*113)
