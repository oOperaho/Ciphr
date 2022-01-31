def caesarciphr(w, k):
    try:
        alphabet, out, l = " abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", "", []

        for letter in w.lower():
            out = alphabet.index(letter) + k
            l.append(alphabet[out])

        return "".join(l)
    except TypeError:
        return "Error! Type a number!"


def caesardecoder(w, k):
    alphabet, out, l = " zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba", "", []

    for letter in w.lower():
        out = alphabet.index(letter) - k
        l.append(alphabet[out])

    return "".join(l)
