#!/usr/bin/python3
# -*- coding: Utf-8 -*
import sys
sys.path.append(r'C:\Users\loupy\OneDrive\Bureau\OPENCLASSROOMS\Projet5\PurBeurre\data')
sys.path.append(r'C:\Users\loupy\OneDrive\Bureau\OPENCLASSROOMS\Projet5\PurBeurre\body')
"""from interface_bdd import BddQueries"""
from data.updateBDD import InsertOrDeleteData
from data.models import History, Product, User, Category, ProductCategory
from pprint import pprint
"""
Main page of the program.
"""

print("WELCOME, I will be able to help you find equivalent products.")
name = input("Let's know us first. What is your name?")
result = User.insert(u_name=name).execute()
print("I",name,"!")
print("Select one of those three choises please!!")

while True:
    main_choice = input(" 1 - Which food do you want to replace?\n 2 - Find my substituted foods.\n 3 - Update the food-database!\n 4 - To quit!\n What is your choice")
    if main_choice == '1': 
        while True:
            while True:
                categories_index_list =[]
                p_categories = Category.select().execute()
                print("I propose you", len(p_categories), "categories!")
                for index, value in enumerate(p_categories):
                    print (index, value )
                    categories_index_list.append(index)
                print("Select one category please!", categories_index_list)
                try:
                    cat_choice =int(input(" Which food do you want to replace?"))
                    c_category = p_categories[cat_choice]
                    print( "You have chosen", c_category, "!") 
                    pass
                except ValueError:
                    continue
                product_categorie_index_list = []
                """query_products_categorie = (ProductCategory._id).select(ProductCategory._id).where(ProductCategory.categories == c_category).limit(20)"""
                for index, value in enumerate(query_products_categorie):
                    print(index, value)
                    product_categorie_index_list.append(index)
                print("Select one product please please!\n", product_categorie_index_list)
                break
            
    if main_choice == '2':
        pass
    if main_choice == "3":
        InsertOrDeleteData.update_all_products()
        pass
    if main_choice == "4":
        print("See you soon! ;-) ")
        break
    else:
        continue



