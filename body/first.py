from datas.insert_data import ResetData
from .choice_cat import ChoiceCategorie
from .product_choice import ChoiceProducts
from .proposed_products import ProposedProducts
from.save_choice import SaveChoice
from .consult_rec import ConsultRec
from datas.insert_data import ResetData



class MainMenu:
    """
    Interface and body of the program.
    """
    def first_menu(user_name):


        while True:
            
            menu_choice=input(user_name+"choisissez parmis ces choix ;-)!\n\
            1-Quel aliment voulez-vous remplacer?\n\
            2-Trouver mes aliments substitués\n\
            3-Inserer les produits dans la base de données,premiére utilisation\n\
            4-Quiter\n\
            [1], [2], [3] ou [4] ?")


            if menu_choice == '1':
                ChoiceCategorie.choice_categorie(user_name)               
              
            if menu_choice == '2':
                ConsultRec.consult_history(user_name)

            if menu_choice == '3':
                ResetData.insert_all_products(user_name)         

            if menu_choice =='4':
                break
            else:
                continue

if __name__ == "__main__":
    pass