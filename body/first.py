import sys
sys.path.insert(0, 'C:\OPENCLASSROOMS\Projet5\PurBeurre\data')
sys.path.insert(1, 'C:\OPENCLASSROOMS\Projet5\PurBeurre\body')
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from data.models import User
from .choice_cat import ChoiceCategories
from .consult_rec import ConsultRec


class MainWindow:
    """
    Interface and body of the program.
    """

    def first_menu(self, window, user_name):

        self.frame2 = tk.Frame(window, bg="#D8BDFF")

        self.frame2_tittle2 = tk.StringVar()
        self.label2_title2 = tk.Label(self.frame2,
         textvariable= self.frame2_tittle2,
        font = ("courrier", 48), bg= "#D8BDFF", fg="white")

        self.frame2_tittle2.set("Salut "+user_name+" !")
        self.label2_title2.pack(pady=25)

        self.frame2_tittle = tk.StringVar()
        self.label2_title = tk.Label(self.frame2,
         textvariable= self.frame2_tittle,
        font = ("courrier", 35), bg= "#D8BDFF", fg="white")
        self.frame2_tittle.set("Choisissez parmis ces choix ;-)")
        self.label2_title.pack(pady=25)

        def first_button():
            self.frame2.destroy()
            ChoiceCategories.Choice_categories(ChoiceCategories, window, MainWindow, user_name)

        def second_button():
            self.frame2.destroy()
            ConsultRec.consult_history(ConsultRec, window, user_name, MainWindow)

        def third_button():
            InsertOrDeleteData.insert_all_products(InsertOrDeleteData)

        def fourth_button():
            self.rep = messagebox.askokcancel (" Attention",
             "Voulez-vous vraiment quitter ce programme ? ") 
            if self.rep == 1:
                window.destroy()
                
        self.first_button = tk.Button(self.frame2,
         text="  Quel aliment voulez-vous remplacer?   ",
          font = ("courrier", 24), bg= "white", fg="#D8BDFF"
           , command=first_button)

        self.first_button.pack(pady=25, side = tk.TOP,
         expand = True, fill = tk.BOTH)

        self.second_button = tk.Button(self.frame2,
         text="  Trouver mes aliments substitués   ", 
         font = ("courrier", 24), bg= "white", fg="#D8BDFF" 
         , command=second_button)

        self.second_button.pack(pady=25, side = tk.TOP,
         expand = True, fill = tk.BOTH)

        self.third_button = tk.Button(self.frame2,
         text="  Inserer les produits dans la base de données, (premiére utilisation)!  ",
          font = ("courrier", 24), bg= "white",
           fg="#D8BDFF" , command=third_button)

        self.third_button.pack(pady=25, side = tk.TOP,
         expand = True, fill = tk.BOTH)
        
        self.fourth_button = tk.Button(self.frame2,
         text="  Quitter!  ", font = ("courrier", 24),
          bg= "white", fg="#D8BDFF" , command=fourth_button)
        self.fourth_button.pack(pady=25,
         side = tk.TOP, expand = True, fill = tk.BOTH)      

        self.frame2.pack(expand=True)
        window.mainloop()

if __name__ == "__main__":
    pass