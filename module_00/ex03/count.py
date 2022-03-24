import string


def text_analyzer(*text):
    """This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."""
    if len(text) < 1:
        text = input("What is the text to analyse ?")
    elif len(text) > 1:
        print("ERROR")
        return
    else:
        text = text[0]

    char_count = len(text)
    upper_count = sum(1 for element in text if element.isupper())
    punc_count = sum(1 for element in text if element in string.punctuation)
    lower_count = sum(1 for element in text if element.islower())
    space_count = text.count(' ')

    print("The text contains ", char_count, " characters:")
    print("- ", upper_count, " upper letters")
    print("- ", lower_count, " lower letters")
    print("- ", punc_count, " punctuation marks")
    print("- ", space_count, " spaces")
