import re
import random


options = {"shuffle", "unique", "ordered"}

def generator(text, sep=" ", option=None):
    """Option is an optional arg, sep is mandatory"""

    if type(text) != str:
        print("ERROR")
        quit(1)
    elif option != None and option in options is False:
        print("ERROR")
        quit(1)
    
    new_text = re.split(sep, text)
    if option == "shuffle":
        last_index = len(new_text) - 1
        while last_index > 0:
            rand_index = random.randint(0, last_index)
            new_text[last_index], new_text[rand_index] = new_text[rand_index], new_text[last_index]
            last_index -= 1
    elif option == "ordered":
        new_text.sort()
    elif option == "unique":
        new_text = list(set(new_text))
        
    for element in new_text :
        print(element)