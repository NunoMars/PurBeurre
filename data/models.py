import peewee
"""from download_products import DataFiles"""


pg_db = peewee.PostgresqlDatabase('Pure_Beurre', user='PureBeurre', password='12345678',
                           host='localhost', port=5432) # Connect to data base.


"""
Defines and create tables.
"""
class User(peewee.Model):
    """ Class to define the User table."""
    id = peewee.PrimaryKeyField()
    u_name = peewee.CharField()

    class Meta:
        database = pg_db
        db_table = 'user'

User.create_table()

class Store(peewee.Model):
    """ Class to define the Store table."""
    stores_tags = peewee.CharField(primary_key=True)

    class Meta:                
        database = pg_db
        db_table = 'store'

Store.create_table()

class Category(peewee.Model):
    """ Class to define the Category table."""    
    categories = peewee.CharField(primary_key=True)

    class Meta:                
        database = pg_db
        db_table = 'category'

Category.create_table()

class Product(peewee.Model):
    """ Class to define the Product table."""
    _id = peewee.BigIntegerField(primary_key=True)
    ingredients_text_fr = peewee.TextField()
    nutrition_grade_fr = peewee.CharField()
    product_name_fr = peewee.TextField()
    url = peewee.TextField()

    class Meta:                
        database = pg_db
        db_table = 'product'

Product.create_table()

class History(peewee.Model):
    """ Class to define the History table."""
    id = peewee.ForeignKeyField( User, backref='history')
    chosen_product = peewee.ForeignKeyField( Product, backref='history')
    remplacement_product = peewee.ForeignKeyField(Product, backref='history')

    class Meta:
        primary_key = peewee.CompositeKey('id', 'chosen_product')                
        database = pg_db
        db_table = 'history'

History.create_table()        

class ProductCategory(peewee.Model):
    """ Class to define the Product category table."""
    _id = peewee.ForeignKeyField ( Product, backref='product_category')
    categories = peewee.ForeignKeyField ( Category, backref='product_category')

    class Meta:
        primary_key = peewee.CompositeKey('_id', 'categories')                
        database = pg_db
        db_table = 'product_category'

ProductCategory.create_table()

class ProductStore(peewee.Model):
    """ Class to define the Product Store table."""
    _id = peewee.ForeignKeyField( Product, backref='product_store')
    stores_tags = peewee.ForeignKeyField(Store, backref='product-store')

    class Meta:
        primary_key = peewee.CompositeKey('_id', 'stores_tags')                
        database = pg_db
        db_table = 'product_store'

ProductStore.create_table()

if __name__ == "__main__":
    pass 