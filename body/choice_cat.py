from data.models import Category
from .product_choice import ChoiceProducts
import tkinter as tk

class ChoiceCategories:
    
   def Choice_categories(self, window, MainWindow, user_name):
        """
        Def to propose the ctegories
        """
        self.p_categories = Category.select().execute()

        self.frame3 = tk.Frame(window, bg="#D8BDFF")

        self.label3_title_var = tk.StringVar()
        self.label3_title = tk.Label(self.frame3,
         textvariable= self.label3_title_var,
        font = ("courrier", 38), bg= "#D8BDFF", fg="white")

        self.label3_title_var.set("Je vous propose "+ str(len(self.p_categories))+ " categories!")
        self.label3_title.pack(pady=25, side = tk.TOP,
         expand = True, fill = tk.BOTH)

        self.label3_title1_var = tk.StringVar()
        self.label3_title1 = tk.Label(self.frame3,
         textvariable= self.label3_title1_var,
        font = ("courrier", 30), bg= "#D8BDFF", fg="white")

        self.label3_title1_var.set("Choisissez parmis ces categories.")

        self.label3_title1.pack(pady=25, side = tk.TOP,
         expand = True, fill = tk.BOTH)

        self.categorieSelect= tk.StringVar()
        self.list_1= tk.Listbox(self.frame3,
         listvariable= self.categorieSelect,
          font = ("courrier", 24), justify=tk.CENTER,
           bg= "white", fg="#D8BDFF", width= 18)

        for index, value in enumerate(self.p_categories):
            self.list_1.insert(index, value)
        self.list_1.pack(pady=25, side = tk.TOP) 

        def clic(evt):
            index = self.list_1.curselection()
            self.c_category = str(self.list_1.get(index)) 

        self.list_1.bind('<ButtonRelease-1>', clic)

        def fifth_button():
            self.frame3.destroy()
            ChoiceProducts.Choice_products(ChoiceProducts,
             window, self.c_category, MainWindow, user_name)


        self.button_t_var = tk.StringVar()
        self.fifth_button = tk.Button(self.frame3,
         textvariable=self.button_t_var,
          font = ("courrier", 20), bg= "white",
           fg="#D8BDFF" , width= 22, command=fifth_button)
           
        self.button_t_var.set("VALIDER VOTRE CHOIX!")
        self.fifth_button.pack(pady=25, side = tk.TOP)

        self.frame3.pack(expand=True)
        window.mainloop()