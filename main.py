#!/usr/bin/python3
# -*- coding: Utf-8 -*
import sys
sys.path.append(r'C:\Users\loupy\OneDrive\Bureau\OPENCLASSROOMS\Projet5\PurBeurre\data')
sys.path.append(r'C:\Users\loupy\OneDrive\Bureau\OPENCLASSROOMS\Projet5\PurBeurre\body')
"""from interface_bdd import BddQueries"""
from data.updateBDD import InsertOrDeleteData

"""
Main page of the program.
"""

print("WELCOME, I will be able to help you find equivalent products.")
name = input("Let's know us first. What is your name?")
print("I",name,"!")
print("Select one of those three choises please!!")

while True:
    main_choice = input(" 1 - Which food do you want to replace?\n 2 - Find my substituted foods.\n 3 - Update the database!\n What is your choice?")
    if main_choice == '1': 
        """while True:
            p_categories = BddQueries.p_categories
            cat_choice = input(" Which food do you want to replace?", print_p_categories())
            if cat_choice == '1':""" 
        pass
    if main_choice == '2':
        pass
    if main_choice == "3":
        InsertOrDeleteData.update_all_products()
        pass
    else:
        continue



