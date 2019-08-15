import sys
sys.path.append("C:\\data")
from data.models import (User,
Store,
Category,
Product,
History,
ProductCategory,
ProductStore)


class BddQueries:

    c_product = []
    proposed_product = []

    def Choice_categories(self):
        """
        Def to propose the ctegories
        """               
        while True:
            categories_index_list = []
            p_categories = Category.select().execute()
            print("I propose you", len(p_categories), "categories!")
            for index, value in enumerate(p_categories):
                print(index, value)
                categories_index_list.append(index)
            print("Select one category please!", categories_index_list)
            try:
                cat_choice = int(input(" Which category do you\
                     want to chose?"))
                if cat_choice in categories_index_list:
                    self.c_category = p_categories[cat_choice]
                    print("You have chosen", self.c_category, "!")
                    break
                else:
                    continue
                pass
            except ValueError:
                continue

    def Choice_products(self):
        """
        Def to propose 25 products.
        """            
        while True:
            product_categorie_index_list = []
            query_products_categorie = (Product.select().join(ProductCategory).join(Category).where(Category.categories == self.c_category).limit(25))

            for index, product in enumerate(query_products_categorie):
                print(index, product.product_name_fr)
                product_categorie_index_list.append(index)
            print("Select one product please\
                 please!\n", product_categorie_index_list)
            try:
                product_choice = int(input(" Which product do you \n\
                    want to chose?"))
                if product_choice in product_categorie_index_list:
                    self.c_product = query_products_categorie[product_choice]
                    print("You have chosen", self.c_product.product_name_fr, "!")

                    print(" Is Id:", self.c_product._id, "\n Namne:",
                    self.c_product.product_name_fr, "\n Web-page:",
                    self.c_product.url,
                    "\n Ingredients :", self.c_product.ingredients_text_fr)
                    pass
                else:
                    continue
                pass
            except ValueError:
                continue
            query_proposed_product = (Product.select().join(ProductCategory).join(Category).where((Product.nutrition_grade_fr == self.c_product.nutrition_grade_fr) & (Category.categories == self.c_category)).limit(1))

            self.proposed_product = query_proposed_product[0]

            print("I've found a equivalent product It's:\n Is Id:",
            self.proposed_product._id,
            "\n Namne:",
             self.proposed_product.product_name_fr,
            "\n Web-page:",
            self.proposed_product.url,
            "\n Ingredients :",
            self.proposed_product.ingredients_text_fr)
            break

    def rec_current_products(self):
        """
        Record the product in dbb
        """      
        while True:
            rec_choice = input("Do you want's record this\
                 chice to the DataBase?\n(Y) or (N)")

            if rec_choice == 'Y' or rec_choice == 'y':
                query_user = User.select().order_by(User.id.desc()).limit(1)
                c_user = query_user[0]
                print(c_user.u_name)
                result = (History.insert(id_id = c_user.id, chosen_product_id = self.c_product._id, remplacement_product_id = self.proposed_product._id).execute())

                print("Done ;-)!")
                break
            else:
                break
            if rec_choice == 'N' or rec_choice == 'n':
                break
            else:
                continue
            continue

    def choice_2(self):
        """
        Def to consulte the history recs.
        """
        while True:
            query_history=History.select()
            history_index_list =[]
            print("You have", len(query_history), "recorded products!")
            for index, value in enumerate(query_history):
                print (index, value )
            break

if __name__ == "__main__":
    BddQueries.Choice_categories(BddQueries)
    BddQueries.Choice_products(BddQueries)
    BddQueries.rec_current_products(BddQueries)
    BddQueries.choice_2(BddQueries)