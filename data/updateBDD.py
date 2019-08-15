import sys
sys.path.append("C:\\data")
from .models import User, Store, Category, Product, History, ProductCategory, ProductStore
from .download_products import DataFiles
from pprint import pprint

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
                print("The DataBase is updated!")
                break
            else:
                break
            if main_choice == 'N' or main_choice == 'n':              
                break 
            else:
                continue 


if __name__ == "__main__":
    update = InsertOrDeleteData.update_all_products()