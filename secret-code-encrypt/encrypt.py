trans = {
    "a": "j",    "b": "d",    "c": "m",    "d": "p",    "e": "f",    "f": "t",    "g": "z",    "h": "x",
    "i": "l",    "j": "a",    "k": "v",    "l": "o",    "m": "k",    "n": "q",    "o": "w",    "p": "r",
    "q": "n",    "r": "c",    "s": "y",    "t": "u",    "u": "i",    "v": "k",    "w": "e",    "x": "h",
    "y": "g",    "z": "s"}

def translate(phrase):

    translation=""

    for letter in phrase:
        trans_letter = trans.get(letter.lower(),letter)
        if letter.isupper():
            trans_letter = trans_letter.upper()
        translation = translation + trans_letter
    return translation

def decode(phrase):

    reverse_trans = {v: k for k, v in trans.items()}
    
    translation = ""
    
    for letter in phrase:
        trans_letter = reverse_trans.get(letter.lower(), letter)
        if letter.isupper():
            trans_letter = trans_letter.upper()
        translation = translation + trans_letter
    return translation

print("\nWelcome to CipherQuest:\nThe Code Chronicles\n")
print("\nHere is the Encrypted Code:\n" + translate(input("Enter a phrase:\n")))
print("\nHere is the Decoded Message:\n" + decode(input("\nEnter an encrypted phrase:\n")))