from datas.models import User, History


class SaveChoice:

    def rec_current_products(c_product, proposed_product, user_name):
        """
        Record the product in dbb
        """
        while True:

            save = input("Voulez-vous enregister votre choix?\n\
                  [O] = Oui  [N] = Non (Retour au menu)")
            if save == "O" or save == "o":
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
            else:
                continue
