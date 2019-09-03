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
    breads = []
    all_products = []
    products_to_inser = []
    categories = []
    stores_tags = []
    _id_and_stores = []
    _id_and_categories = []

    def __init__ (self):
        print("L'importation a commencé, commençons le travail maintenant!")

    def download_and_clean_all_products(self):
        """
        Modul to download, clean and parse the products-file.
        """

        link1 = "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=Snacks%20sucr%C3%A9s&tagtype_1=categories&tag_contains_1=contains&tag_1=Snacks%20sucr%C3%A9s&sort_by=unique_scans_n&page_size=1000&axis_x=energy&axis_y=products_n&action=process&page=2&json=1"
        link2 = "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=pizza&tagtype_1=categories&tag_contains_1=contains&tag_1=pizza&sort_by=product_name&page_size=500&axis_x=energy&axis_y=products_n&action=process&page=2&json=1"
        link3 = "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=boissons&tagtype_1=categories&tag_contains_1=contains&tag_1=boissons&sort_by=product_name&page_size=1000&axis_x=energy&axis_y=products_n&action=process&page=2&json=1"
        link4 = "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=Produits%20laitiers&tagtype_1=categories&tag_contains_1=contains&tag_1=Produits%20laitiers&sort_by=unique_scans_n&page_size=1000&axis_x=energy&axis_y=products_n&action=process&page=2&json=1"
        link5 = "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=Pains&tagtype_1=categories&tag_contains_1=contains&tag_1=Pains&sort_by=unique_scans_n&page_size=1000&axis_x=energy&axis_y=products_n&action=process&page=2&json=1"    
        
        links = [link1, link2, link3, link4, link5]
        categories_list = ["Snacks", "Pizza", "Boissons", "Produits laitiers", "Pains"]

        for i,j  in zip(links, categories_list):
            r = requests.get(i)
            self.current_product = json.loads(r.content)# rec the data in a variable

            print("Nous avons maintenant 1000 produits téléchargés!")

            self.current_product = CleanFile.clean_data(self.current_product, j) # cleanup the data

            if len(self.current_product) != 0:
                self.all_products.extend(self.current_product)
            print("Nous avons ", len( self.all_products),"produits téléchargées et nettoyées!")

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

    DataFiles.download_and_clean_all_products(DataFiles)
    DataFiles.add_and_clean_products_to_inser(DataFiles)
    DataFiles.add_and_clean_all_categories(DataFiles)
    DataFiles.add_and_clean_all_stores(DataFiles)
    DataFiles.add_and_clean_all_id_and_categories(DataFiles)
    DataFiles.add_and_clean_all_id_and_stores(DataFiles)

