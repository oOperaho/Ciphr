def caesarencoder(w, k):
    if k <= 26:
        alphabet, out, l = " abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", "", []

        for letter in w:
            out = alphabet.index(letter) + k
            l.append(alphabet[out])

        return "".join(l)
    else:
        return "Key only between 1-26!"


def caesardecoder(w, k):
    if k <= 26:
        alphabet, out, l = " zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba", "", []

        for letter in w:
            out = alphabet.index(letter) + k
            l.append(alphabet[out])

        return "".join(l)
    else:
        return "Key only between 1-26!"
