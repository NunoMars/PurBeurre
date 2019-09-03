import sys
sys.path.insert(0, 'C:\OPENCLASSROOMS\Projet5\PurBeurre\data')

from data.models import (User,
 Product,
  ProductCategory,
   ProductStore,
    History,
     Store,
      Category)

import tkinter as tk

class ConsultRec:

    def consult_history(self, window, user_name, MainWindow):
        """
        Def to consulte the history recs.
        """
        self.frame8 = tk.Frame(window, bg="#D8BDFF")
        self.frame9 = tk.Frame(window, bg="#D8BDFF")
        self.label8_title_var = tk.StringVar()


        query_user = User.select().where(User.u_name == user_name)
        c_user = query_user[0]

        chosen_product = Product.alias()
        remplacement_product = Product.alias()

        self.query = (History
        .select(History,
            chosen_product,
            remplacement_product, User)
        .join(chosen_product,
            on=(History.chosen_product == chosen_product._id))
        .switch(History)
        .join(remplacement_product,
            on=(History.remplacement_product == remplacement_product._id))
        .join(User, on=(History.id == User.id))
        .where(History.id == c_user.id))

        self.label8_title_var.set(c_user.u_name.capitalize()+" vous avez "+ str(len(self.query))+ " produits enregistrés!")
        self.label8_title = tk.Label(self.frame8,
        textvariable= self.label8_title_var,
        font = ("courrier", 30), bg= "#D8BDFF", fg="white")

        self.label8_title.pack(pady=18, side = tk.TOP,
            expand = True, fill = tk.BOTH)

        self.sb3 = tk.Scrollbar(self.frame8)
        self.sb3.pack(pady=18, side=tk.RIGHT, fill = tk.BOTH)


        self.list_3= tk.Listbox(self.frame8,
          font = ("courrier", 15), bg= "white", fg="#D8BDFF", width= 90 )

        for index, item in enumerate(self.query):
            query1 = Product.select().where(Product._id == item.chosen_product._id)
            query2 = Product.select().where(Product._id == item.remplacement_product._id)
            self.list_3.insert(index, "PRODUIT CHOISI: "+query1[0].product_name_fr+"\nREMPLACE PAR: "+query2[0].product_name_fr)

        self.list_3.pack(pady=18, side = tk.TOP)
  
        self.list_3.configure(yscrollcommand=self.sb3.set)
        self.sb3.configure(command=self.list_3.yview)

        """self.label8_title_var.set(user_name.capitalize() +" Vous n'avez pas de produits enregistrés!")"""
        """self.canvas3_text_var.set("Rien a afficher")"""

        def eleventh_button():
            self.frame8.destroy()
            self.frame9.destroy()
            MainWindow.first_menu(MainWindow, window, user_name)


        self.eleventh_button_var = tk.StringVar()
        self.eleventh_button = tk.Button(self.frame9,
            textvariable=self.eleventh_button_var,
            font = ("courrier", 15), bg= "white",
            fg="#D8BDFF" , command=eleventh_button)

        self.eleventh_button_var.set("Retour au menu")
        self.eleventh_button.pack(pady=25, side = tk.TOP)

        self.frame8.pack()
        self.frame9.pack()
        window.mainloop()

if __name__ == "__main__":
    pass
