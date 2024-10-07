"""
Description: Automated Teller Machine (ATM) Simulator
Author: Tyler Jablonski
Date: October 6th 2024
"""
import random
import os
from time import sleep

menudict = {
    "uppercase": {
        "Deposit": "D",
        "Withdraw": "W",
        "Quit": "Q",
    },
    "lowercase": {
        "deposit": "d",
        "withdraw": "w",
        "quit": "q",
    }
}

# Assigning the values to the variables and formatting them properly
balance = random.randint(-1000, 10000)

title_text = "PIXELL RIVER FINANCIAL"
title_text = title_text.center(40)

subheading = "ATM Simulator"
subheading = subheading.center(40)

balance_text = "Your current balance is: ${balance:,.2f} "
balance_text = balance_text.center(50)

deposit_text = "Deposit: D"
deposit_text = deposit_text.center(40)

withdraw_text = "Withdraw: W"
withdraw_text = withdraw_text.center(40)

quit_text = "Quit: Q"
quit_text = quit_text.center(40)

invalid_text = "INVALID SELECTION"
invalid_text = invalid_text.center(40)

insufficient_text = "INSUFFICIENT FUNDS"
insufficient_text = insufficient_text.center(40)


# Start the loop for selection
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    # Printing the selection menu
    print("****************************************")
    print(title_text)
    print(subheading)
    print(balance_text.format(balance=balance))
    print(deposit_text)
    print(withdraw_text)
    print(quit_text)
    print("****************************************")


    # Prompt for user input inside the loop
    selection = input("Enter your selection: ").lower()  # Convert to lowercase for easy comparison

    # Handle Quit option
    if selection == menudict["lowercase"]["quit"]: 
        break  # Exit the loop after quitting

    # Check if the selection is valid
    if selection in menudict["lowercase"].values():
    
        # Handle Deposit selection
        if selection == menudict["lowercase"]["deposit"]:
            amount = input("Enter the amount: ")
            balance += float(amount)
            print("****************************************")
            print(balance_text.format(balance=balance))
            print("****************************************")
            sleep(3)
        
        # Handle Withdraw selection
        elif selection == menudict["lowercase"]["withdraw"]:
            amount = input("Enter the amount: ")
                
            if float(amount) > balance:
                print("****************************************")
                print(insufficient_text)
                print("****************************************")
            else:
                balance -= float(amount)
                print("****************************************")
                print(balance_text.format(balance=balance))
                print("****************************************")
            sleep(3)

    # Handle invalid selection
    else:
        print("****************************************")
        print(invalid_text)
        print("****************************************")
        sleep(2)  # Pause to allow the user to see the invalid input message
