"""
Description: Automated Teller Machine  (ATM) Simulator
Author: Tyler Jablonski
Date: October 6th 2024
"""
import random

menudict = {
    "Deposit": "D",
    "Withdraw": "W",
    "Quit": "Q"
 }


balance = random.randint(-1000,10000)

title_text = "PIXELL RIVER FINANCIAL"
title_text = title_text.center(40)

subheading =  "ATM Simulator"
subheading =  subheading.center(40)

balance_text =  "Your current balance is: ${balance:,.2f} "
balance_text = balance_text.center(50)

deposit_text = "Deposit: D"
deposit_text  = deposit_text.center(40)

withdraw_text =  "Withdraw: W"
withdraw_text =  withdraw_text.center(40)

quit_text = "Quit: Q"
quit_text =  quit_text.center(40)




print("****************************************")
print(title_text)
print(subheading)
print(balance_text.format(balance = balance))
print(deposit_text)
print(withdraw_text)
print(quit_text)
print("****************************************")