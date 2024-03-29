from datas.models import (
 Category,
 Product,
 ProductCategory,
 ProductStore)
from .proposed_products import proposed_product


def choice_products(c_category, user_name):
    """
    Def to propose 25 products each time and choose one.
    """
    print(user_name, " vous avez choisi ", c_category, " !")

    query_products_categorie = (
        Product.select()
        .join(ProductCategory)
        .join(Category)
        .where(Category.categories == c_category))

    index_products_list = []
    products_dict = {}

    for index, product in enumerate(query_products_categorie):
        products_dict.update({index: product.product_name_fr})
        index = str(index)
        index_products_list.append(index)
    print("Nous avons", len(index_products_list), "produits!")
    n = 0  # Page mumber
    t = 25  # Number or products
    i = 0  # Index

    while True:
        try:
            for i in range(n, t):
                print(i, products_dict[i])
                i += 1
        except KeyError:  # Set products-list to zero and restart
            n = 0
            t = 25
            i = 0
            continue
        p_choice = input(
                "Choisissez parmis ces produits!\n" +
                "Entrez son numero pour choisir!\n" +
                "[C] pour continuer [Q]" +
                "pour quiter et revenir au menu ! ;-)")

        if p_choice == 'C' or p_choice == 'c':
            n = t + 1
            t = t + 25
            i = i + 1
            continue

        if p_choice == 'Q' or p_choice == 'q':
            break
        if p_choice in index_products_list:
            p_choice = int(p_choice)
            product_choice = products_dict[p_choice]
            print(
                user_name,
                "Vous avez choisi : ", product_choice, " !")
            proposed_product(
                product_choice, c_category, user_name)
            break
