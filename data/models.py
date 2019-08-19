from peewee import *

pg_db = PostgresqlDatabase('Pure_Beurre', user='PureBeurre', password='12345678',
                           host='localhost', port=5432) # Connect to data base.


"""
Defines and create tables.
"""

class User(Model):
    """ Class to define the User table."""
    id = PrimaryKeyField()
    u_name = CharField(unique=True)

    class Meta:
        database = pg_db
        db_table = 'user'

class Store(Model):
    """ Class to define the Store table."""
    stores_tags = CharField(primary_key=True)

    class Meta:                
        database = pg_db
        db_table = 'store'

class Category(Model):
    """ Class to define the Category table."""    
    categories = CharField(primary_key=True)

    class Meta:                
        database = pg_db
        db_table = 'category'

class Product(Model):
    """ Class to define the Product table."""
    _id = CharField(primary_key=True)
    ingredients_text_fr = TextField()
    nutrition_grade_fr = CharField()
    product_name_fr = TextField()
    url = TextField()

    class Meta:                
        database = pg_db
        db_table = 'product'

class History(Model):
    """ Class to define the History table."""
    id = PrimaryKeyField()
    _id = ForeignKeyField(User, backref='history')
    chosen_product = ForeignKeyField(Product, related_name = 'chosen_product ', backref='history')
    remplacement_product = ForeignKeyField(Product, related_name = 'remplacement_product', backref='history')

    class Meta:          
        database = pg_db
        db_table = 'history'

class ProductCategory(Model):
    """ Class to define the Product category table."""
    _id = ForeignKeyField (Product, backref='product_category')
    categories = ForeignKeyField (Category, backref='product_category')

    class Meta:
        primary_key = CompositeKey('_id', 'categories')                
        database = pg_db
        db_table = 'product_category'

class ProductStore(Model):
    """ Class to define the Product Store table."""
    _id = ForeignKeyField(Product, backref='product_store')
    stores_tags = ForeignKeyField(Store, backref='product-store')

    class Meta:
        primary_key = CompositeKey('_id', 'stores_tags')                
        database = pg_db
        db_table = 'product_store'

if __name__ == "__main__":
    User.create_table()
    Store.create_table()
    Category.create_table()
    Product.create_table()
    History.create_table()
    ProductCategory.create_table()
    ProductStore.create_table() 