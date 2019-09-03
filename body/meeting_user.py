from datas.models import User
from .first import MainMenu


class Hi:

    def meeting_user():
        while True:
            user_name=input("BIENVENUE\n Je peut vous aider à trouver un produit équivalent.\nFaisons d'habord connaiscance, quel est votre nom?")
            if user_name == '' or  user_name == ' ':
                continue
            else:
                user_name = user_name.capitalize()
                User.get_or_create(u_name=user_name)
                MainMenu.first_menu(user_name)
                break

if __name__ == "__main__":
    Ni.meeting_user()