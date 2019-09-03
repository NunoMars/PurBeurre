from datas.models import (User,
Category,
Product,
ProductCategory,
ProductStore)
from .save_choice import SaveChoice
import webbrowser


class ProposedProducts:
    
    def proposed_product(
     product_choice, c_category,
     user_name):

        query_product = (Product.select()
        .where(Product.product_name_fr == product_choice))
        c_product = query_product[0]

        print(str(c_product.product_name_fr).upper(),
         "!\n Son identifiant est:", str(c_product._id),
         "\n ses ingredients :\n", str(c_product.ingredients_text_fr))



        def seventh_button():
            webbrowser.open_new(self.c_product.url)

        query_proposed_product = (Product.select()
        .join(ProductCategory).join(Category)
        .where((Product.nutrition_grade_fr == c_product.nutrition_grade_fr)\
             & (Category.categories == c_category))
        .order_by(fn.Rand()).limit(1))

        proposed_product = query_proposed_product[0]


        print(str(proposed_product.product_name_fr).upper(),
         "!\n Son identifiant est:", str(proposed_product._id),
         "\n ses ingredients :\n", str(proposed_product.ingredients_text_fr))

        def eighth_button():
            webbrowser.open_new(self.proposed_product.url)

        def save_products_chossen(self):
            self.save=input("Enregister choix")
            SaveChoice.rec_current_products(SaveChoice,
             self.c_product, self.proposed_product, user_name)

        def back_to_menu(self):

            MainWindow.first_menu(MainWindow, window, user_name)


