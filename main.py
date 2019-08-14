#!/usr/bin/python3
# -*- coding: Utf-8 -*
from body.interface_bdd import BddQueries
from data.updateBDD import InsertOrDeleteData
from data.models import User
"""
Main page of the program.
"""

print("WELCOME, I will be able to help you find equivalent products.")
name = input("Let's know us first. What is your name?")
result = User.insert(u_name=name).execute()
print("I", name, "!")
print("Select one of those three choises please!!")

while True:
    main_choice = input(" 1 - Which food do you want to replace?\n\
         2 - Find my substituted foods.\n\
              3 - Update the food-database!\n\
                   4 - To quit!\n What is your choice")
    if main_choice == '1':
        BddQueries.Choice_categories(BddQueries)
        BddQueries.Choice_products(BddQueries)
        BddQueries.rec_current_products(BddQueries)

    if main_choice == '2':
        BddQueries.choice_2(BddQueries)

    if main_choice == "3":
        InsertOrDeleteData.update_all_products()
        pass
    if main_choice == "4":
        print("See you soon! ;-) ")
        break
    else:
        continue

if __name__ == "__main__":
    pass