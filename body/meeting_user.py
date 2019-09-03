from data.models import User
from .choice_cat import ChoiceCategories
from .first import MainWindow
import tkinter as tk

class Hi:

    window = tk.Tk()
    window.title("PUR BEURRE APP")
    window.geometry("1080x1080")
    window.minsize(600, 400)
    window.iconbitmap("icon.ico")
    window.config(background = "#D8BDFF")
    c_product = []
    proposed_product = []


    def meeting_user(self):
        self.frame0 = tk.Frame(self.window, bg="#D8BDFF")

        self.var_label_tittle = tk.StringVar()
        self.var_label_tittle.set("BIENVENUE\n Je peut vous aider à trouver un produit équivalent.\nFaisons d'habord connaiscance, quel est votre nom?")
        
        self.label_title = tk.Label(self.frame0,
         textvariable= self.var_label_tittle,
        font = ("courrier", 30), bg= "#D8BDFF", fg="white")

        self.label_title.pack(pady=25)

        self.name= tk.StringVar()
        self.entry = tk.Entry(self.frame0,
         textvariable= self.name,
          font = ("courrier", 24), bg= "white", fg="#D8BDFF") 

        self.entry.pack(pady=25)

        def get_entry():
            self.user_name = str(self.name.get())
            while True:
                if self.user_name == '':
                    tk.messagebox.showinfo("Ups, entrez votre nom", "Ne soyez-pas timide ! ;-) Quel est votre nom ?")
                    break
                else:
                    User.get_or_create(u_name=self.user_name.capitalize())
                    self.frame0.destroy()
                    MainWindow.first_menu(MainWindow, self.window, self.user_name.capitalize())
                    break


        self.button = tk.Button(self.frame0,
         text="  Valider   ", font = ("courrier", 24),
          bg= "white", fg="#D8BDFF" ,  width= 18, 
           command=get_entry)

        self.button.pack(pady=25)

        self.frame0.pack(expand=True)  
        self.window.mainloop()   
