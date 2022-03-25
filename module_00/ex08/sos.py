import sys


morse_code = {
    'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 
    'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 
    'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 
    'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', 
    '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', 
}

assert len(sys.argv) > 1, "ERROR"

translated = ""
for x in sys.argv[1:]:
    x = x.upper()
    for letter in x:
        if letter is " ":
            translated += " / "
        elif letter.isalnum() is False:
            print("ERROR")
            quit(1)
        elif letter in morse_code:
            translated += morse_code[letter]
            translated += " "
    translated += " / "
translated = translated[:len(translated) - 3]
print(translated)
