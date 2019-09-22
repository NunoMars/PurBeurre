from datas.models import (
    User,
    Product,
    ProductCategory,
    ProductStore,
    History,
    Store,
    Category)


def consult_history(user_name):
    """
    Def to consulte the history recs.
    """
    user_name = user_name.capitalize()
    User.get_or_create(u_name=user_name)
    
    query_user = User.select().where(User.u_name == user_name)
    c_user = query_user[0]

    chosen_product = Product.alias()
    remplacement_product = Product.alias()

    query = (
        History.select(
            History, chosen_product,
            remplacement_product, User)
        .join(chosen_product, on=(
            History.chosen_product == chosen_product._id))
        .switch(History)
        .join(
            remplacement_product,
            on=(History.remplacement_product == remplacement_product._id))
        .join(User, on=(History.id == User.id))
        .where(History.id == c_user.id))

    print(
        c_user.u_name,
        " vous avez ",
        len(query),
        " produits enregistrés!")

    for index, item in enumerate(query):
        query1 = Product.select().where(
            Product._id == item.chosen_product._id)
        query2 = Product.select().where(
            Product._id == item.remplacement_product._id)
        print(
            index, "PRODUIT CHOISI: "+query1[0].product_name_fr +
            "\nREMPLACE PAR: "+query2[0].product_name_fr)

if __name__ == "__main__":
    consult_history(user_name)
