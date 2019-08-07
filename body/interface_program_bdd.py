import peewee
from dataclasses import dataclass
from just_do_it import Basquets
from pprint import pprint

pg_db = peewee.PostgresqlDatabase('Pure_Beurre', user='PureBeurre', password='12345678',
                           host='localhost', port=5432) # Connect to data base.

class User(peewee.Model):
    """ Class to define the User table."""
    id = peewee.PrimaryKeyField()
    u_name = peewee.CharField()

    class Meta:
        database = pg_db
        db_table = 'user'

class Store(peewee.Model):
    """ Class to define the Store table."""
    stores_tags = peewee.CharField(primary_key=True)

    class Meta:                
        database = pg_db
        db_table = 'store'

class Category(peewee.Model):
    """ Class to define the Category table."""    
    categories_tags = peewee.CharField(primary_key=True)

    class Meta:                
        database = pg_db
        db_table = 'category'

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

class History(peewee.Model):
    """ Class to define the History table."""
    user = peewee.ForeignKeyField( User, backref='history')
    chosen_product = peewee.ForeignKeyField( Product, backref='history')
    remplacement_product = peewee.ForeignKeyField(Product, backref='history')

    class Meta:
        primary_key = peewee.CompositeKey('user', 'chosen_product')                
        database = pg_db
        db_table = 'history'
 
class ProductCategory(peewee.Model):
    """ Class to define and access ProductCategory table."""
    _id = peewee.ForeignKeyField ( Product, backref='product_category')
    categories_tags = peewee.ForeignKeyField ( Category, backref='product_category')

    class Meta:
        primary_key = peewee.CompositeKey('_id', 'categories_tags')                
        database = pg_db
        db_table = 'product_category'

class ProductStore(peewee.Model):
    """ Class to define and access ProductStore table."""
    _id = peewee.ForeignKeyField( Product, backref='product_store')
    stores_tags = peewee.ForeignKeyField(Store, backref='product-store')

    class Meta:
        primary_key = peewee.CompositeKey('_id', 'stores_tags')                
        database = pg_db
        db_table = 'product_store'

@dataclass
class Querries:
    '''
    Class to interface with the Data-Base.
    '''
    proposed_categories = list

    query= Category.select()
    proposed_categories = query.execute()

    """p_categories = Basquets.nike(proposed_categories)"""
    for item in proposed_categories:
        print(item)

pg_db.close()    
