import requests, json
from clear_data import CleanFile
from dataclasses import dataclass
from pprint import pprint

@dataclass
class DataFiles:
    """
    Class allowing to download and filter the products to be inserted in the Data Base.
    """
    snacks = list
    pizzas = list
    drinks = list
    cheese = list
    pasta = list
    products = list
    products_to_inser = list
    categories = list
    stores_tags = list
    id_and_stores = list
    _id_and_categories = list

    print( "Importation started let's do some work now!")

    def download_and_clean_snacks():
        """
        Modul to download, clean and parse the products-file.
        """

        link1 = "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=snacks&sort_by=unique_scans_n&page_size=10&axis_x=energy&axis_y=products_n&action=process&page=2&json=1"    
        r = requests.get(link1)
        snacks = json.loads(r.content)# rec the data in a variable
        print("We have now 1000 products downloaded!")
        snacks = CleanFile.clean_data(snacks) # cleanup the data
        print("We have now ", len( snacks ), "products downloaded and cleaned!")
        return snacks
    
    def download_and_clean_pizzas():        
        """
        Modul to download, clean and parse the products-file.
        """
       
        link2 = "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=pizza&sort_by=unique_scans_n&page_size=10&axis_x=energy&axis_y=products_n&action=process&page=2&json=1"
        r = requests.get(link2)
        pizzas = json.loads(r.content)# rec the data in a variable
        print("We have now 1000 products downloaded!")
        pizzas = CleanFile.clean_data(pizzas)
        print("We have now", len( pizzas ), "pizzas downloaded and cleaned!")
        return pizzas

    def download_and_clean_drinks():
        """
        Modul to download, clean and parse the products-file.
        """

        link3 = "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=boissons&sort_by=unique_scans_n&page_size=10&axis_x=energy&axis_y=products_n&action=process&page=2&json=1"
        r = requests.get(link3)
        drinks = json.loads(r.content)
        print("We have now 3000 products downloaded!")
        drinks = CleanFile.clean_data(drinks)
        print("We have now", len( drinks ), "dinks downloaded and cleaned!")
        return drinks

    def download_and_clean_cheese():
        """
        Modul to download, clean and parse the products-file.
        """      

        link4 = "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=fromages&sort_by=unique_scans_n&page_size=10&axis_x=energy&axis_y=products_n&action=process&page=2&json=1"
        r = requests.get(link4)
        cheese = json.loads(r.content)
        print("We have now 4000 products downloaded!")
        cheese = CleanFile.clean_data(cheese)
        print("We have now", len( cheese ), "cheese downloaded and cleaned!")
        return cheese

    def download_and_clean_pasta():
        """
        Modul to download, clean and parse the products-file.
        """

        link5 = "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=pâtes&sort_by=unique_scans_n&page_size=10&axis_x=energy&axis_y=products_n&action=process&page=2&json=1"
        r = requests.get(link5)
        pasta = json.loads(r.content)
        print("We have now 5000 products downloaded! Now let's clean them ;-) !")
        pasta = CleanFile.clean_data(pasta)
        print("We have now", len(pasta), "pasta downloaded, and cleaned!")
        return pasta
      
    def add_and_clean_all_products():
        """
        Modul to add, clean and parse all products-file.
        """
        products = DataFiles.snacks + Datafiles.pizzas + DataFiles.drinks + DataFiles.cheese + DataFiles.pasta      
        products = CleanFile.eliminate_duplicate_products(products)
        print("After a hard cleaning job we have", len(products), "good products! let's put them in the Data_Base!")
        return products

    def add_and_clean_all_products():
        """
        Modul to prepare products-file to insert in database.
        """
        products = DataFiles.products 
        products_to_inser = CleanFile.products_to_inser(products) 
        print(len(self.products_to_inser), "Products are ready to insert.")
        return products_to_inser

    def add_and_clean_all_categories():
        """
        Modul to prepare categories-file to insert in database.
        """ 
        categories = CleanFile.select_categories(products)
        print("We have ", len(self.categories),"categories!")
        return categories

    def add_and_clean_all_stores():
        """
        Modul to prepare stores-file to insert in database.
        """
        stores_tags = CleanFile.select_stores_tags(products)
        print("Wee have ", len(self.stores_tags),"stores!")
        return stores_tags

    def add_and_clean_all_id_and_stores():
        """
        Modul to prepare id_and_sores-file to insert in database.
        """ 
        _id_and_stores = CleanFile.select_id_and_stores_tags(products)
        print(len(self._id_and_stores), "Id and stores are ready to insert.")
        return _id_and_stores

    def add_and_clean_all_id_and_categories():
        """
        Modul to prepare id_and_categorie-file to insert in database.
        """
        _id_and_categories = CleanFile.select_id_and_categories(products)
        print(len(self._id_and_categories), "Id and categories are ready to insert.")
        return _id_and_categories

if __name__ == "__main__":
    DataFiles.download_and_clean_snacks()
    DataFiles.download_and_clean_pizzas()
    DataFiles.download_and_clean_drinks()
    DataFiles.download_and_clean_cheese()
    DataFiles.download_and_clean_pasta()
    DataFiles.add_and_clean_all_products()
    DataFiles.add_and_clean_all_categories()
    DataFiles.add_and_clean_all_stores()
    DataFiles.add_and_clean_all_id_and_categories()
    DataFiles.add_and_clean_all_id_and_stores()

