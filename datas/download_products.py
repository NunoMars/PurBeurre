import requests
import json
from .clear_data import (
    clean_data,
    eliminate_duplicate_products,
    products_to_inser,
    select_categories,
    select_stores_tags,
    select_id_and_stores_tags,
    select_id_and_categories
)


class DataFiles:
    """
    Class allowing to download and filter the
     products to be inserted in the Data Base.
    """
    all_products = []
    products_to_inser = []
    categories = []
    stores_tags = []
    _id_and_stores = []
    _id_and_categories = []

    def __init__(self):
        print("L'importation a commencé, commençons le travail maintenant!")

    def download_and_clean_all_products(self):
        """
        Modul to download, clean and parse the products-file.
        """
        print("Connexion a l'API afin de telecharger les produits")

        categories_list = [
            "Snacks",
            "Pizza",
            "Boissons",
            "Produits laitiers",
            "Pains",
            "Plats préparés"]

        for item in categories_list:
            r = requests.get(
                "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=" +
                item + "&tagtype_1=categories&tag_contains_1=contains&tag_1=" +
                item + "&sort_by=unique_scans_n&page_size=1000&axis_x=energy&axis_y=products_n&action=process&page=2&json=1"
                )
            self.current_product = json.loads(r.content)

            self.current_product = clean_data(
                self.current_product, item)

            if len(self.current_product) != 0:
                self.all_products.extend(self.current_product)

        self.all_products = eliminate_duplicate_products(
            self.all_products)
        """
        Prepare products-file to insert in database.
        """
        self.products_to_inser = products_to_inser(self.all_products)
        """
        Prepare categories-file to insert in database.
        """

        self.categories = select_categories(self.all_products)

        """
        Prepare stores-file to insert in database.
        """
        self.stores_tags = select_stores_tags(self.all_products)

        """
        Prepare id_and_sores-file to insert in database.
        """
        self._id_and_stores = select_id_and_stores_tags(
            self.all_products)

        """
        Prepare id_and_categorie-file to insert in database.
        """
        self._id_and_categories = select_id_and_categories(
            self.all_products)

if __name__ == "__main__":
    DataFiles()
