import re


def reformat(txt):
    ntxt = re.sub("[^a-zA-Z]", "", txt)
    return ntxt


def caesarencoder(w, k):
    alphabet, out, l = " abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", "", []

    for letter in reformat(w):
        out = alphabet.index(letter) + k
        l.append(alphabet[out])

    return "".join(l)


def caesardecoder(w, k):
    alphabet, out, l = " zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba", "", []

    for letter in reformat(w):
        out = alphabet.index(letter) + k
        l.append(alphabet[out])

    return "".join(l)
