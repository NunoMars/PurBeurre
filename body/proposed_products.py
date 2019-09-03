from data.models import (User,
Category,
Product,
ProductCategory,
ProductStore)
from .save_choice import SaveChoice
from peewee import fn
import tkinter as tk
import webbrowser


class ProposedProducts:
    
    def proposed_product(self, window, product_choice, c_category, MainWindow, user_name):
        self.frame6 = tk.Frame(window, bg="#D8BDFF")

        self.query_product = (Product.select()
        .where(Product.product_name_fr == product_choice))
        self.c_product = self.query_product[0]

        self.label5_title_var = tk.StringVar()
        self.label5_title = tk.Label(self.frame6,
         textvariable= self.label5_title_var,
        font = ("courrier", 30), bg= "#D8BDFF", fg="white")

        self.label5_title_var.set("Votre selection "+ user_name.capitalize()+" !")
        self.label5_title.pack(pady=10, side = tk.TOP,
         expand = True, fill = tk.BOTH)

        self.canvas1_text_var = tk.StringVar()
        self.canvas1 = tk.Canvas(self.frame6,
         width=900, height=300, background="white")

        self.canvas1_text_var.set(str(self.c_product.product_name_fr).upper() + "!\n Son identifiant est:"+ str(self.c_product._id) +"\n ses ingredients :\n"+ str(self.c_product.ingredients_text_fr))
        self.canvas1.create_text(450, 150,
         text=self.canvas1_text_var.get(),
          font="courrier 15", fill="#D8BDFF",
           justify="center", width=850)

        self.canvas1.pack(pady= 10, side = tk.TOP)

        def seventh_button():
            webbrowser.open_new(self.c_product.url)

        self.seventh_button_var = tk.StringVar()
        self.seventh_button = tk.Button(self.frame6,
         textvariable=self.seventh_button_var,
          font = ("courrier", 18), bg= "white",
           fg="#D8BDFF" , command=seventh_button)

        self.seventh_button_var.set("Voir Sa Page Internet?")
        self.seventh_button.pack(pady=10)

        self.label7_title_var = tk.StringVar()
        self.label7_title = tk.Label(self.frame6,
         textvariable= self.label7_title_var,
        font = ("courrier", 30), bg= "#D8BDFF", fg="white")

        self.label7_title_var.set("Je vous propose")
        self.label7_title.pack(pady=10, side = tk.TOP, expand = True)

        self.query_proposed_product = (Product.select()
        .join(ProductCategory).join(Category)
        .where((Product.nutrition_grade_fr == self.c_product.nutrition_grade_fr) & (Category.categories == c_category))
        .order_by(fn.Rand()).limit(1))

        self.proposed_product = self.query_proposed_product[0]
        self.canvas2_text_var = tk.StringVar()
        self.canvas2 = tk.Canvas(self.frame6,
         width=900, height=300, background="white") 

        self.canvas2_text_var.set(str(self.proposed_product.product_name_fr).upper() + "!\n Son identifiant est:"+ str(self.proposed_product._id) +"\n ses ingredients :\n"+ str(self.proposed_product.ingredients_text_fr))
        self.canvas2.create_text(450, 150,
         text=self.canvas2_text_var.get(),
          font="courrier 15", fill="#D8BDFF",
           justify="center", width=850)

        self.canvas2.pack(pady= 10, side = tk.TOP)

        def eighth_button():
            webbrowser.open_new(self.proposed_product.url)

        self.eighth_button_var = tk.StringVar()
        self.eighth_button = tk.Button(self.frame6,
         textvariable=self.seventh_button_var,
          font = ("courrier", 18), bg= "white",
           fg="#D8BDFF" , command=eighth_button)

        self.eighth_button_var.set("Voir Sa Page Internet?")
        self.eighth_button.pack(pady=10)

        def ninth_button():
            SaveChoice.rec_current_products(SaveChoice,
             self.c_product, self.proposed_product, user_name)

        self.ninth_button_var = tk.StringVar()
        self.ninth_button = tk.Button(self.frame6,
         textvariable=self.ninth_button_var,
          font = ("courrier", 18), bg= "white",
           fg="#D8BDFF" , command=ninth_button)
        self.ninth_button_var.set("Enregister choix")

        self.ninth_button.pack(pady=10, side = tk.RIGHT)

        def tenth_button():
            self.frame6.destroy()
            MainWindow.first_menu(MainWindow, window, user_name)


        self.tenth_button_var = tk.StringVar()
        self.tenth_button = tk.Button(self.frame6,
         textvariable=self.tenth_button_var,
          font = ("courrier", 18), bg= "white",
           fg="#D8BDFF" , command=tenth_button)

        self.tenth_button_var.set("Retour au menu")
        self.tenth_button.pack(pady=10, side = tk.LEFT)

        self.frame6.pack(expand=True)
        window.mainloop()