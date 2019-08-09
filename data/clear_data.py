from collections import OrderedDict
from pprint import pprint
class CleanFile:
    """
    Class to filter the data.
    """

    def clean_data (file):
        """
        Clean the downloaded file and choose juste that wee need
        """
        products = file["products"] # reach to the list os the products
        wanted_labels = ["_id",
        "product_name_fr",
        "stores_tags",
        "url",
        "ingredients_text_fr",
        "nutrition_grade_fr"] #list of the labels to search, test and add to the new list
        
        print ( "Let's do some clean-up job!")
        processed_products = [] 

        for product in products:# the list contains dictionaries
            current_product = {}
            o_current_product = {}
            current_categories_values = []
            for p_label, p_value in product.items():
                if p_label == "categories":
                    if len(p_value) != 0:
                        if p_value != None or "null" or " ":
                            item = p_value.split(",")
                            if item != []:
                                for i in item:
                                    if i[0] == " ":
                                        i = i[1:]
                                        current_categories_values.append(i)
            if len(current_categories_values) != 0:
                current_product.update({"categories": current_categories_values})
                            
            for p_label, p_value in product.items(): #test if the labels and values are in the dictionary
                if p_label in wanted_labels:# add to current_product if key and value are present
                    if len(p_value) != 0:
                        if p_value != None or "null":       
                            current_product.update({p_label: p_value})

            if len(current_product) == 7:
                o_current_product = OrderedDict(sorted(current_product.items(), key=lambda t: t[0]))
                if o_current_product not in processed_products: 
                    processed_products.append(o_current_product)
     
        return processed_products #return cleaned file

    def eliminate_duplicate_products(file):
        """
        Eliminate duplicate products.
        """
        products = file
        print ( "Let's do some clean-up job!")
        processed_products = [] 

        for product in products:# the list contains dictionaries
            if product not in processed_products: 
                processed_products.append(product)
        return processed_products #return cleaned file

    def products_to_inser (file):
        """
        Prepare products file to insert to Data-Base.
        """
        products = file # reach to the list os the products
     
        wanted_labels = ["_id",
        "product_name_fr",
        "url",
        "ingredients_text_fr",
        "nutrition_grade_fr"] #list of the labels to search, test and add to the new list
        
        print ( "Let's do some clean-up job!")
        processed_products = [] 

        for product in products:# the list contains dictionaries
            current_product = {}
            for p_label, p_value in product.items():
                if p_label in wanted_labels:     
                    current_product.update({p_label: p_value})# add to current_product if key and value are present
            processed_products.append(current_product)
                    
        return processed_products #return cleaned file

    
    def select_categories(file):
        """
        Search and records all categories for insert in data_base.
        """
        products = file
        current_category = []
        processed_categories = []
        for product in products:
            for category in product["categories"]:
                if category not in current_category:
                    current_category.append(category)
        for item in current_category:
            processed_categories.append({"categories" : item})
        return processed_categories
       
    def select_stores_tags(file):
        """
        Search and records all store_tags for insert in data_base.
        """
        products = file
        current_stores_tags =[]
        processed_stores_tags = []
        for product in products:
            for store in product["stores_tags"]:
                if store not in current_stores_tags:
                    current_stores_tags.append(store)
        for item in current_stores_tags:
            processed_stores_tags.append({"stores_tags": item})
        return processed_stores_tags


    def select_id_and_stores_tags(file):
        """
        Search and records all id and store_tags for insert in to data_base.
        """
        products = file
        processed_id_and_stores = []
        for product in products:
            for store in product["stores_tags"]:
                if {'_id': product['_id'], "stores_tags": store} not in processed_id_and_stores:
                    processed_id_and_stores.append({'_id': product['_id'], "stores_tags": store})
        return processed_id_and_stores

    def select_id_and_categories(file):
        """
        Search and records all id and categories for insert in to data_base.
        """
        products = file
        processed_id_and_categories = []
        for product in products:
            for category in product["categories"]:
                if {'_id': product['_id'], "categories": category} not in processed_id_and_categories:
                    processed_id_and_categories.append({'_id': product['_id'], "categories": category})
        return processed_id_and_categories