def caesarciphr(w, k):
    alphabet, out, l = " abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", "", []

    for letter in w.lower():
        out = alphabet.index(letter) + k
        l.append(alphabet[out])

    return "".join(l)
