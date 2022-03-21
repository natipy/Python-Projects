import json
import string
from random import choice
import urllib
import os

UPPER = string.ascii_uppercase

def scrap_words():
    """
    This function is used to scrap english words from  web retun these words radomly.
    """
    with open("words.text") as file:
        words = json.load(file)
    return choice(words).upper()

def play():
    words = scrap_words()
    assert words
    used_word = set()
    corret = set()
    live = len(words)
    word = []
    while live:
        word = [i.upper() if i in corret else "-" for i in words]
        if ''.join(word) == words:break
        print("USED WORDS : {}".format(' '.join(used_word).upper())) 
        print(' '.join(word))
        print("LIVE : {live}".format(live=live))
        try:put = input("> ").upper()[0]
        except:continue
        os.system('cls')
        if put in UPPER:
            if put in words:
                corret.add(put)
                print("Correct You get it!")
            elif put.lower() in used_word or put.upper() in used_word:
                print("Already used this latter.")
                live-=1
            else:
                print("Not in word")
                live-=1
            used_word.add(put)
        else:
            print("Invalid Input")
            live-=1
        
    if not live:
        print("You lose :(\nthe word was {word}".format(word=words))
    else:
        print("You won!!",''.join(word))
play()