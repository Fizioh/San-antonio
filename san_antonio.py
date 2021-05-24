# -*- coding: utf8 -*-
import random
import json

quotes = [
    "Nakama desho ne ?", 
    "Ikuze mina !",
    "Kaizoku ore wa naru",
    "Oden ni soro"
]


def read_value_from_json():
    values = []
    
    with open('characters.json') as f:
        data = json.load(f)
    for entry in data:
        values.append(entry['character'])
    return values
    
def get_random_item(my_list):
    rand_numb = random.randint(0, len(my_list) -1)
    item = my_list[rand_numb]
    return item

def random_character():
    all_values = read_value_from_json()
    return get_random_item(all_values)

def capitalize(words):
    for word in words:
        word.capitalize()
        
def message(character, quote):
    capitalize(character)
    capitalize(quote)
    return "{} a dit : {}".format(character, quote)

user_answer = input("Tapez entrée pour connaitre une autre citation ou B pour quitter")

while user_answer != "B":
    print(message(random_character(), get_random_item(quotes)))
    user_answer = input("Tapez entrée pour connaitre une autre citation ou B pour quitter")

    