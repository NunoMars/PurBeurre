#!/usr/bin/python3
# -*- coding: Utf-8 -*
import sys
sys.path.append(r'C:\Users\loupy\OneDrive\Bureau\OPENCLASSROOMS\Projet5\PurBeurre\data')
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
        pass
    if main_choice == '2':
        pass
    if main_choice == "3":
        InsertOrDeleteData.update_all_products()
        
        break
    else:
        continue



