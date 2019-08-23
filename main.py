#!/usr/bin/python3
# -*- coding: Utf-8 -*
import sys
sys.path.append("C:\\data")
sys.path.append("C:\\body")
from body.interface_bdd import BddQueries
from data.updateBDD import InsertOrDeleteData

class MainPaje:
    """
    Main page of the program.
    """

    BddQueries.meeting_user(BddQueries)

    while True:
        main_choice = input(" 1 - Quel aliment voulez-vous remplacer?\n\
    2 - Trouver mes aliments substitués.\n\
    3 - Mettre à jour la base de données!\n\
    4 - Quitter!\n\
    Quel est votre choix? [1], [2], [3], [4]")

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
            print("À bientôt! ;-) ")
            break
        else:
            continue

if __name__ == "__main__":
    pass