from peewee import fn
from data.models import (User,
Store,
Category,
Product,
History,
ProductCategory,
ProductStore)


class BddQueries:
    """
    Interface and body of the program.
    """

    c_product = []
    proposed_product = []


    def meeting_user(self):
        print("BIENVENU/E, je peut vous aider à trouver un produit équivalent.")
        self.user_name = input("Faisons d'habord connaiscance, quel est votre nom?")
        user, u_name = User.get_or_create(u_name=self.user_name)
        print("Salut", self.user_name, "!")            


    def Choice_categories(self):
        """
        Def to propose the ctegories
        """               
        while True:
            categories_index_list = []
            p_categories = Category.select().execute()
            print("Je vous propose", len(p_categories), "categories!")
            for index, value in enumerate(p_categories):
                print(index, value)
                categories_index_list.append(index)
            print("Sélectionnez une catégorie s'il vous plaît!", categories_index_list)
            try:
                cat_choice = int(input("Quelle catégorie voulez-vous choisir?"))
                if cat_choice in categories_index_list:
                    self.c_category = p_categories[cat_choice]
                    print("Vous avez selectionné", self.c_category, "!")
                    break
                else:
                    continue
                pass
            except ValueError:
                continue

    def Choice_products(self):
        """
        Def to propose 25 random products.
        """            
        while True:
            product_categorie_index_list = []
            query_products_categorie = (Product.select()
            .join(ProductCategory)
            .join(Category)
            .where(Category.categories == self.c_category)
            .order_by(fn.Random()).limit(25))

            for index, product in enumerate(query_products_categorie):
                print(index, product.product_name_fr)
                product_categorie_index_list.append(index)
            print("Sélectionnez un produit s'il vous plaît!", product_categorie_index_list)
            try:
                product_choice = int(input("Quel produit voulez-vous choisir?"))
                if product_choice in product_categorie_index_list:
                    self.c_product = query_products_categorie[product_choice]
                    print("Vous avez choisi", self.c_product.product_name_fr, "!")
                    print(" Son identifiant est:", self.c_product._id, "\n Son nom:",
                    self.c_product.product_name_fr, "\n Sa page internet:",
                    self.c_product.url,
                    "\n ses ingredients :", self.c_product.ingredients_text_fr)
                    pass
                else:
                    continue
                pass
            except ValueError:
                continue
            query_proposed_product = (Product.select()
            .join(ProductCategory).join(Category)
            .where((Product.nutrition_grade_fr == self.c_product.nutrition_grade_fr) & (Category.categories == self.c_category))
            .order_by(fn.Random()).limit(1))

            self.proposed_product = query_proposed_product[0]

            print("J'ai trouvé un produit équivalent C'est:\n Son identifiant:",
            self.proposed_product._id,
            "\n son nom:",
             self.proposed_product.product_name_fr,
            "\n Sa page internet:",
            self.proposed_product.url,
            "\n Ses ingredients :",
            self.proposed_product.ingredients_text_fr)
            break

    def rec_current_products(self):
        """
        Record the product in dbb
        """      
        while True:
            rec_choice = input("Voulez-vous enregistrer?\n\(Y) or (N)")

            if rec_choice == 'Y' or rec_choice == 'y':
                query_user = User.select().order_by(User.id.desc()).limit(1)

                c_user = query_user[0]
                result = (History.insert(_id = c_user.id,
                 chosen_product_id = self.c_product._id,
                 remplacement_product_id = self.proposed_product._id)
                 .execute())

                print("Fait ;-)!")
                break
            else:
                break
            if rec_choice == 'N' or rec_choice == 'n':
                break
            else:
                continue
            continue

    def choice_2(self):
        """
        Def to consulte the history recs.
        """
        while True:
            query_user = User.select().where(User.u_name == self.user_name)
            c_user = query_user[0]

            chosen_product = Product.alias()
            remplacement_product = Product.alias()

            query = (History
            .select(History,
             chosen_product,
              remplacement_product, User)
            .join(chosen_product,
             on=(History.chosen_product == chosen_product._id))
            .switch(History)
            .join(remplacement_product,
             on=(History.remplacement_product == remplacement_product._id))
            .join(User, on=(History._id == User.id))
            .where(History._id == c_user.id))

            print(c_user.u_name,"Vous avez", len(query), "produits enregistrés!")
            for item in query:
                query1 = Product.select().where(Product._id == item.chosen_product._id)

                query2 = Product.select().where(Product._id == item.remplacement_product._id)

                print("PRODUIT CHOISI:",
                 query1[0].product_name_fr,
                 "REMPLACE PAR:", query2[0].product_name_fr)
            break

if __name__ == "__main__":
    BddQueries.meeting_user(BddQueries)
    BddQueries.Choice_categories(BddQueries)
    BddQueries.Choice_products(BddQueries)
    BddQueries.rec_current_products(BddQueries)
    BddQueries.choice_2(BddQueries)