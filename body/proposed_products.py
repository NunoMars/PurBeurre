from datas.models import (User,
Category,
Product,
ProductCategory,
ProductStore)
import webbrowser
from peewee import fn
from .save_choice import SaveChoice


class ProposedProducts:
    
    def proposed_product(
    product_choice,
    c_category,
    user_name):


        query_product = (Product.select()
        .where(Product.product_name_fr == product_choice))
        c_product = query_product[0]

        print(str(c_product.product_name_fr).upper(),
        "!\n Son identifiant est:\n", c_product._id,
        "\n Ses ingredients :\n", c_product.ingredients_text_fr,
        "\n Son site internet est :\n", c_product.url)

        print("Je vous propose le produit suivant! ")

        query_proposed_product = (Product.select()
        .join(ProductCategory).join(Category)
        .where((Product.nutrition_grade_fr == c_product.nutrition_grade_fr)\
            & (Category.categories == c_category))
        .order_by(fn.Rand()).limit(1))

        proposed_product = query_proposed_product[0]


        print(str(proposed_product.product_name_fr).upper(),
        "!\n Son identifiant est:\n", proposed_product._id,
        "\n Ses ingredients sont:\n", proposed_product.ingredients_text_fr,
        "\n Son site internet est :\n", proposed_product.url)

        while True:
            web_page_ask2 = input("Voulez-vous voir leur page internet?\n  [O] = Oui  [N] = Non")
            if web_page_ask2 == "O" or web_page_ask2 == "o":
                webbrowser.open_new(c_product.url)
                webbrowser.open_new(proposed_product.url)                    
                break
            if web_page_ask == "N" or web_page_ask == "n":
                break
            else:
                continue
        
        SaveChoice.rec_current_products(c_product, proposed_product, user_name)



