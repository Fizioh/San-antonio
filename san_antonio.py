# -*- coding: utf8 -*-
import random

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
def get_random_quote(my_list):
    rand_numb = random.randint(0, len(my_list) -1)
    item = my_list[rand_numb]
    return item
user_answer = input("Tapez entrée pour connaitre une autre citation ou B pour quitter")



while user_answer != "B":
    print(get_random_quote(quotes))
    user_answer = input("Tapez entrée pour connaitre une autre citation ou B pour quitter")
    
for character in characters:
    name_character = character.capitalize()
    print (name_character)

print(get_random_quote(quotes))

    