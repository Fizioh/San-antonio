# -*- coding: utf8 -*-
quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = [
    "alvin et les Chipmunks", 
    "Babar", 
    "betty boop", 
    "calimero", 
    "casper", 
    "le chat potté", 
    "Kirikou"
]

user_answer = input("Tapez entrée pour connaitre une autre citation ou B pour quitter")

if user_answer == "B":
    pass
elif user_answer == "C":
    print("Ce n'est pas la bonne réponse...")
else:
    pass


def show_random_quote(my_list):
    item = my_list[1]
    print(item)
    return "Le programme est terminé"

print(show_random_quote(quotes))

    