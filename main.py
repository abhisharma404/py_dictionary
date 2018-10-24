import json
from difflib import get_close_matches

# load the dictionary json
data=json.load(open("data.json"))

def translate(word):
    word=word.lower()
    if word in data:
        print(data[word])
    elif len(get_close_matches(word,data.keys()))>0:
        valid=get_close_matches(word,data.keys())[0].lower()
        if(word==valid):
            print(data[get_close_matches(word,data.keys())[0]])
        else:
            print("Did you mean %s instead...?" %get_close_matches(word,data.keys())[0])
            option=input("Enter Y for YES N for NO : ")
            if option=="Y":
                print(data[get_close_matches(word,data.keys())[0]])
    else:
        print("No such word found!")

word=input("Enter word you want to search for...: ")

translate(word)
