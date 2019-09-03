from datas.models import (
Category,
Product,
ProductCategory,
ProductStore)
from .proposed_products import ProposedProducts


class ChoiceProducts:

    def Choice_products(c_category, user_name):
        """
        Def to propose 25 random products.
        """
        query_products_categorie = (Product.select()
        .join(ProductCategory)
        .join(Category)
        .where(Category.categories == c_category))

        index_products_list = []
        products_dict= {}
        
        for index, product in enumerate(query_products_categorie):
            index_products_list.append(index)
            products_dict.update({index: product.product_name_fr})

        n = 0
        t = 24
        while n < t:
            for n in products_dict:
                print(n, products_dict[n])

        product_choice =input("Choisissez parmis ces produits, C pour continuer!")
        if product_choice == 'C' or product_choice == 'c':
            n = t + 1
            t = t + 25

