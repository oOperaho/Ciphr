def caesarciphr(w, k):
    try:
        alphabet, out, l = " abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", "", []

        for letter in w.lower():
            out = alphabet.index(letter) + k
            l.append(alphabet[out])

        return "".join(l)
    except ValueError:
        return "Error! Type a number!"

