import sys
sys.path.append(r'C:\Users\loupy\OneDrive\Bureau\OPENCLASSROOMS\Projet5\PurBeurre\data')
from models import User, Store, Category, Product, History, ProductCategory, ProductStore
from pprint import pprint

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
                        break
                    else:
                        continue 
                    pass
                except ValueError:
                    continue
            while True:
                product_categorie_index_list = []
                query_products_categorie = (Product.select().join(ProductCategory).join(Category)
                .where(Category.categories == c_category).limit(25))

                for index, product in enumerate(query_products_categorie):
                    print(index, product.product_name_fr)
                    product_categorie_index_list.append(index)
                print("Select one product please please!\n", product_categorie_index_list)
                try:
                    product_choice =int(input(" Which product do you want to chose?"))
                    if product_choice in product_categorie_index_list:
                        c_product = query_products_categorie[product_choice]
                        print( "You have chosen", c_product.product_name_fr, "!")
                        print(" Is Id:",c_product._id,"\n Namne:", c_product.product_name_fr,"\n Web-page:",c_product.url,"\n Ingredients :", c_product.ingredients_text_fr)
                        pass
                    else:
                        continue
                    pass
                except ValueError:
                    continue
                query_proposed_product = (Product.select().join(ProductCategory).join(Category)
                .where((Product.nutrition_grade_fr == c_product.nutrition_grade_fr) & (Category.categories == c_category)).limit(1))
                proposed_product = query_proposed_product[0]
                print("I've found a equivalent product It's:\n Is Id:",proposed_product._id,"\n Namne:", proposed_product.product_name_fr,"\n Web-page:",proposed_product.url,"\n Ingredients :", proposed_product.ingredients_text_fr)
                break
            continue

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