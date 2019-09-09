from .models import(
    User,
    Store,
    Category,
    Product,
    History,
    ProductCategory,
    ProductStore
)
from .download_products import DataFiles


class ResetData:
    """
    Class to insert or delete products into Models tables
    """
    def insert_all_products(user_name):
        """
        Delete all products in dbb
        """
        print(
            "Vous êtes sur? ",
            user_name,
            " Voulez-vous vraiment metre-à-jour la base de données?")

        reset_data = input("  [O]=Oui  [N] = Non   :")

        if reset_data == 'O' or reset_data == 'o':
            """
            Import the products from download_products
            """
            DataFiles.download_and_clean_all_products(DataFiles)

            categories = DataFiles.categories
            print("Nous avous, à présent ", len(categories),
                  "categories!")
            stores_tags = DataFiles.stores_tags
            print("Nous avous aussi ", len(stores_tags),
                  "magasins!")
            products_to_inser = DataFiles.products_to_inser
            print("Nous avons ", len(products_to_inser),
                  "produits téléchargées et nettoyées!")
            _id_and_categories = DataFiles._id_and_categories
            print(len(
                _id_and_categories),
                "Les identifiants et les catégories sont prêts à être insérés."
                )
            _id_and_stores = DataFiles._id_and_stores
            print(len(
                _id_and_stores),
                "Les identifiants et les magasins sont prêts à être insérés.")

            """
            Insert all products in database
            """
            print("Insértion de tous les nouveaux produits!")

            for data_dict in categories:
                try:
                    Category.create(**data_dict)
                except:
                    pass
            print("Insértion de Categories terminé!")

            for data_dict in stores_tags:
                try:
                    Store.create(**data_dict)
                except:
                    pass
            print("Insértion de Magasins terminé!")

            for data_dict in products_to_inser:
                try:
                    Product.create(**data_dict)
                except:
                    pass
            print("Insértion des Produits terminé!")

            for data_dict in _id_and_categories:
                try:
                    ProductCategory.create(**data_dict)
                except:
                    pass
            print("Insértion de Categories de Produits terminé!")

            for data_dict in _id_and_stores:
                try:
                    ProductStore.create(**data_dict)
                except:
                    pass
            print("Insértion des magasins por chaque produit terminé!")

            print(
                "Les produits sont, à present,",
                " sauvegardées dans la base de données!")
