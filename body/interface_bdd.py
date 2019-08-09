import sys
sys.path.append(r'C:\Users\loupy\OneDrive\Bureau\OPENCLASSROOMS\Projet5\PurBeurre\data')
from models import User, Store, Category, Product, History, ProductCategory, ProductStore
from dataclasses import dataclass

@dataclass
class BddQueries:
    p_categories = list    
    
    def proposed_categories():
        d_categories = Category.select()
        """d_categories = query.execute()"""
        for i in d_categories:
            print(i)
        sorted_categories = RandList.rand_propose(d_categories)
        for i in range(20):
            for item in sorted_categories:
                p_categories.append({i:item})
test = BddQueries.proposed_categories()
print(test)
