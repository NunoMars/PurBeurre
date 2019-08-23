import sys
sys.path.append("C:\\data")
import requests, json
from clear_data import CleanFile

class DataFiles:
    """
    Class allowing to download and filter the products to be inserted in the Data Base.
    """
    snacks = []
    pizzas = []
    drinks = []
    cheese = []
    pasta = []
    all_products = []
    products_to_inser = []
    categories = []
    stores_tags = []
    _id_and_stores = []
    _id_and_categories = []

    def __init__ (self):
        print("L'importation a commencé, commençons le travail maintenant!")

    def download_and_clean_snacks(self):
        """
        Modul to download, clean and parse the products-file.
        """

        link1 = "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=snacks&sort_by=unique_scans_n&page_size=1000&axis_x=energy&axis_y=products_n&action=process&page=2&json=1"    
        r = requests.get(link1)
        self.snacks = json.loads(r.content)# rec the data in a variable
        print("Nous avons maintenant 1000 produits téléchargés!")
        self.snacks = CleanFile.clean_data(self.snacks) # cleanup the data
        print("Nous avons ", len( self.snacks ),"collations téléchargées et nettoyées!")


    def download_and_clean_pizzas(self):        
        """
        Modul to download, clean and parse the products-file.
        """
       
        link2 = "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=pizza&sort_by=unique_scans_n&page_size=500&axis_x=energy&axis_y=products_n&action=process&page=2&json=1"
        r = requests.get(link2)
        self.pizzas = json.loads(r.content)# rec the data in a variable
        print("Nous avons maintenant plus 1000 produits téléchargés!")
        self.pizzas = CleanFile.clean_data(self.pizzas)
        print("Nous avons", len(self.pizzas), "pizzas téléchargées et nettoyées!")

    def download_and_clean_drinks(self):
        """
        Modul to download, clean and parse the products-file.
        """

        link3 = "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=boissons&sort_by=unique_scans_n&page_size=1000&axis_x=energy&axis_y=products_n&action=process&page=2&json=1"
        r = requests.get(link3)
        self.drinks = json.loads(r.content)
        print("Nous avons maintenant plus 1000 produits téléchargés!")
        self.drinks = CleanFile.clean_data(self.drinks)
        print("Nous avons", len( self.drinks ), "boissons téléchargées et nettoyées!")

    def download_and_clean_cheese(self):
        """
        Modul to download, clean and parse the products-file.
        """      

        link4 = "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=fromages&sort_by=unique_scans_n&page_size=1000&axis_x=energy&axis_y=products_n&action=process&page=2&json=1"
        r = requests.get(link4)
        self.cheese = json.loads(r.content)
        print("Nous avons maintenant plus 1000 produits téléchargés!")
        self.cheese = CleanFile.clean_data(self.cheese)
        print("Nous avons", len( self.cheese ), "fromages téléchargées et nettoyées!")

    def download_and_clean_pasta(self):
        """
        Modul to download, clean and parse the products-file.
        """

        link5 = "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=pâtes&sort_by=unique_scans_n&page_size=1000&axis_x=energy&axis_y=products_n&action=process&page=2&json=1"
        r = requests.get(link5)
        self.pasta = json.loads(r.content)
        print("Nous avons maintenant 5000 produits téléchargés! Maintenant, nettoyons-les ;-) !")
        self.pasta = CleanFile.clean_data(self.pasta)
        print("Nous avons", len(self.pasta), "pâtes téléchargées et nettoyées!")
      
    def add_and_clean_all_products(self):
        """
        Modul to add, clean and parse all products-file.
        """
        if len(self.snacks) != 0:
            self.all_products.extend(self.snacks)
        if len(self.pizzas) != 0:
            self.all_products.extend(self.pizzas)
        if len(self.drinks) != 0:
            self.all_products.extend(self.drinks)
        if len(self.cheese) != 0:
            self.all_products.extend(self.cheese)
        if len(self.pasta) != 0:
            self.all_products.extend(self.pasta)

        self.all_products = CleanFile.eliminate_duplicate_products(self.all_products)
        print("Après un dur travail de nettoyage, nous avons",
         len(self.all_products),
         "bons produits! Mettons-les dans la base de données!")

    def add_and_clean_products_to_inser(self):
        """
        Modul to prepare products-file to insert in database.
        """

        self.products_to_inser = CleanFile.products_to_inser(self.all_products) 
        print(len(self.products_to_inser), " produits sont prêts à être insérés.")


    def add_and_clean_all_categories(self):
        """
        Modul to prepare categories-file to insert in database.
        """ 
        self.categories = CleanFile.select_categories(self.all_products)
        print("Nous avous, à présent ", len(self.categories),"categories!")

    def add_and_clean_all_stores(self):
        """
        Modul to prepare stores-file to insert in database.
        """
        self.stores_tags = CleanFile.select_stores_tags(self.all_products)
        print("Nous avous aussi ", len(self.stores_tags),"magasins!")

    def add_and_clean_all_id_and_stores(self):
        """
        Modul to prepare id_and_sores-file to insert in database.
        """ 
        self._id_and_stores = CleanFile.select_id_and_stores_tags(self.all_products)
        print(len(self._id_and_stores), "Les identifiants et les magasins sont prêts à être insérés.")


    def add_and_clean_all_id_and_categories(self):
        """
        Modul to prepare id_and_categorie-file to insert in database.
        """
        self._id_and_categories = CleanFile.select_id_and_categories(self.all_products)
        print(len(self._id_and_categories),"Les identifiants et les catégories sont prêts à être insérés.")

if __name__ == "__main__":

    DataFiles.download_and_clean_snacks(DataFiles)
    DataFiles.download_and_clean_pizzas(DataFiles)
    DataFiles.download_and_clean_drinks(DataFiles)
    DataFiles.download_and_clean_cheese(DataFiles)
    DataFiles.download_and_clean_pasta(DataFiles)
    DataFiles.add_and_clean_all_products(DataFiles)
    DataFiles.add_and_clean_products_to_inser(DataFiles)
    DataFiles.add_and_clean_all_categories(DataFiles)
    DataFiles.add_and_clean_all_stores(DataFiles)
    DataFiles.add_and_clean_all_id_and_categories(DataFiles)
    DataFiles.add_and_clean_all_id_and_stores(DataFiles)

