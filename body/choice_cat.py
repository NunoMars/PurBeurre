from datas.models import Category
from .product_choice import ChoiceProducts

class ChoiceCategorie:
    
   def choice_categorie(user_name):
        """
        Def to propose the ctegories
        """
        p_categories = Category.select().execute()

        print(user_name," Je vous propose ",
         len(p_categories), " categories!")

        print("Choisissez parmis ces categories.")

        index_list = []
        categories_dict = {}
    
        while True:
            for index, value in enumerate(p_categories):
                print(index, value)
                index_list.append(index)
                categories_dict.update({index: value})            
            try:
                select_index=input("Quelle categorie voulez vous consulter "+
                str(index_list)+" ?")

                if int(select_index) in index_list:
                    c_category = categories_dict[int(select_index)]
                    ChoiceProducts.Choice_products(c_category, user_name)
                    break
                else:
                    continue
            except ValueError:
                continue            
