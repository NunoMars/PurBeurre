import sys
sys.path.append(r'C:\Users\loupy\OneDrive\Bureau\OPENCLASSROOMS\Projet5\PurBeurre\data')
from models import User, Store, Category, Product, History, ProductCategory, ProductStore


class BddQueries:
    
    def Choice_1(self):
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
                    cat_choice =int(input(" Which category do you want to chose?"))
                    if cat_choice in categories_index_list:
                        c_category = p_categories[cat_choice]
                        print( "You have chosen", c_category, "!")
                    else:
                        continue 
                    pass
                except ValueError:
                    continue
                product_categorie_index_list = []
                query_products_categorie = ProductCategory.select()
                    
                for index, value in enumerate(query_products_categorie):
                    print(index, value)
                    product_categorie_index_list.append(index)
                print("Select one product please please!\n", product_categorie_index_list)
                try:
                    product_choice =int(input(" Which category do you want to chose?"))
                    pass
                except ValueError:
                    pass
                break

    def choice_2(self):
        while True:
            query_history = History.select()
            history_index_list =[]
            p_categories = Category.select().execute()
            print("You have", len(query_history), "recorded products!")
            for index, value in enumerate(query_history):
                print (index, value )
                categories_index_list.append(index)
            break

if __name__ == "__main__":
    BddQueries.Choice_1(BddQueries)
    BddQueries.choice_2(BddQueries)