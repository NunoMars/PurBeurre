from datas.models import User, History


def rec_current_products(c_product, proposed_product, user_name):
    """
    Record the product in dbb
    """
    while True:

        save = input("Voulez-vous enregister votre choix?\n\
                [O] = Oui  [N] = Non (Retour au menu)")
        if save == "O" or save == "o":
            user_name = user_name.capitalize()
            User.get_or_create(u_name=user_name)
            query_user = User.select().where(User.u_name == user_name)
            c_user = query_user[0]

            result = (History.insert(
                id_id=c_user.id,
                chosen_product_id=c_product._id,
                remplacement_product_id=proposed_product._id)
                .execute(),
            )
            print("Choix sauvagerdé;-) FAIT")
            break
        if save == "N" or save == "n":
            break
        else:
            continue
