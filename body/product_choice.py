from data.models import (
Category,
Product,
ProductCategory,
ProductStore)
from .proposed_products import ProposedProducts
import tkinter as tk

class ChoiceProducts:

    def Choice_products(self, window, c_category,  MainWindow, user_name):
        """
        Def to propose 25 random products.
        """
        self.frame4 = tk.Frame(window, bg="#D8BDFF")
        self.frame5 =tk.Frame(window, bg="#D8BDFF" )

        self.query_products_categorie = (Product.select()
        .join(ProductCategory)
        .join(Category)
        .where(Category.categories == c_category))

        self.label4_title_var = tk.StringVar()
        self.label4_title = tk.Label(self.frame4,
         textvariable= self.label4_title_var,
        font = ("courrier", 30), bg= "#D8BDFF", fg="white")

        self.label4_title_var.set("Choisissez parmis ces produits")
        self.label4_title.pack(pady=18, side = tk.TOP,
         expand = True, fill = tk.BOTH)

        self.sb = tk.Scrollbar(self.frame4)
        self.sb.pack(pady=18, side=tk.RIGHT, fill = tk.BOTH)

        self.productSelect= tk.StringVar()
        self.list_2= tk.Listbox(self.frame4,
         listvariable= self.productSelect,
          font = ("courrier", 18), bg= "white", fg="#D8BDFF", width= 65 )

        for index, product in enumerate(self.query_products_categorie):
            self.list_2.insert(index, product.product_name_fr)
        self.list_2.pack(pady=18, side = tk.TOP)
  
        self.list_2.configure(yscrollcommand=self.sb.set)
        self.sb.configure(command=self.list_2.yview)

        def clic(evt):
            index = self.list_2.curselection()
            self.product_choice = str(self.list_2.get(index)) 

        self.list_2.bind('<ButtonRelease-1>', clic)

        def sixth_button():
            self.frame4.destroy()
            self.frame5.destroy()
            ProposedProducts.proposed_product(ProposedProducts,
             window, self.product_choice, c_category, MainWindow, user_name)

        self.sixth_button_var = tk.StringVar()
        self.sixth_button = tk.Button(self.frame5,
         textvariable=self.sixth_button_var,
          font = ("courrier", 24), bg= "white",
           fg="#D8BDFF" , command=sixth_button)

        self.sixth_button_var.set("VALIDER VOTRE CHOIX!")
        self.sixth_button.pack(pady=18, expand= True,
         side = tk.TOP, fill = tk.BOTH)
        
        self.frame4.pack(expand=True)
        self.frame5.pack(expand=True)
        window.mainloop()

if __name__ == "__main__":
    pass

