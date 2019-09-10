from datas.insert_data import insert_all_products
from .choice_cat import choice_categorie
from .consult_rec import consult_history


def main_menu(user_name):
    """
    Interface and body of the program.
    """

    while True:
        menu_choice = input(
            user_name+"  choisissez parmis ces choix ;-)!\n\
        1-Quel aliment voulez-vous remplacer?\n\
        2-Trouver mes aliments substitués\n\
        3-Inserer les produits dans la base de" +
            "données (premiére utilisation)\n\
        4-Quiter\n\
        [1], [2], [3] ou [4] ?")

        if menu_choice == '1':
            choice_categorie(user_name)
        if menu_choice == '2':
            consult_history(user_name)
        if menu_choice == '3':
            insert_all_products(user_name)
        if menu_choice == '4':
            break
        else:
            continue

if __name__ == "__main__":
    main_menu(user_name)
