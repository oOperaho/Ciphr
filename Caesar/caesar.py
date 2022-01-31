import re


def reformat(txt):
    ntxt = re.sub("[^a-zA-Z]", "", txt)
    return ntxt


def caesarencoder(w, k):
    try:
        alphabet, out, l = " abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", "", []

        for letter in reformat(w):
            out = alphabet.index(letter) + k
            l.append(alphabet[out])

        return "".join(l)
    except TypeError:
        return "Error! Type a number as key!"


def caesardecoder(w, k):
    try:
        alphabet, out, l = " zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba", "", []

        for letter in w.lower():
            out = alphabet.index(letter) + k
            l.append(alphabet[out])

        return "".join(l)
    except TypeError:
        return "Error! Type a number as key!"
