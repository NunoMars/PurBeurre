import sys
from models import User, Store, Category, Product, History, ProductCategory, ProductStore
from download_products import DataFiles

class InsertOrDeleteData:
    """
    Class to insert or delete products into Models tables
    """
    def update_all_products():
        """
        Delete all products in dbb
        """        
        while True:
            main_choice = input("Do you realy want's to update the DataBase?\n(Y) or (N)")
            if main_choice == 'Y' or main_choice == 'y':
                print("Clearing all tables!!!") 
                query5 = ProductCategory.delete()
                f = query5.execute()
        
                query6 = ProductStore.delete()
                g = query6.execute() 
                    
                query4 = History.delete()
                e = query4.execute()
        
                query1 = Store.delete()
                b = query1.execute()
        
                query2 = Category.delete()
                c = query2.execute()
        
                query3 = Product.delete()
                d = query3.execute()
        
                """
                Import the products from download_products
                """
                files = DataFiles.load_products_openfoodfacts()
                categories = DataFiles.categories
                stores_tags = DataFiles.stores_tags
                products_to_inser = DataFiles.products_to_inser
                _id_and_categories = DataFiles._id_and_categories
                _id_and_stores = DataFiles._id_and_stores
                """
                Insert all products in database
                """
                print("Insertint all new products!")
                Category.insert_many(categories).execute()
                Store.insert_many(stores_tags).execute()
                Product.insert_many(products_to_inser).execute()
                ProductCategory.insert_many(_id_and_categories).execute()
                ProductStore.insert_many(_id_and_stores).execute()

            if main_choice == 'N' or main_choice == 'n':              
                break 
            else:
                continue 
       

if __name__ == "__main__":
    pass