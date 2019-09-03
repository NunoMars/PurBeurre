    
from data.models import User, History  

class SaveChoice:    
    def rec_current_products(self, c_product, proposed_product, user_name):
        """
        Record the product in dbb
        """      
        query_user = User.select().where(User.u_name == user_name)
        c_user = query_user[0]

        result = (History.insert(id_id = c_user.id,
        chosen_product_id = c_product._id,
        remplacement_product_id = proposed_product._id)
        .execute())

        print("Fait ;-)!")
