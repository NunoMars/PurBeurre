from .first import main_menu


def meeting():
    while True:
        user_name = input(
            "BIENVENUE\n Je peut vous aider à trouver un produit équivalent.\n\
                Faisons d'habord connaiscance, quel est votre nom?   :")
        if user_name == '' or user_name == ' ':
            continue
        else:
            main_menu(user_name)
            break

if __name__ == "__main__":
    meeting_user()
