def caesarciphr(w, k):
    w = str(input("Enter the word to encrypt: ")).strip().lower().replace(" ", "")
    k = int(input("Enter the caesar key (0-26): "))
    alphabet, out, l = " abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", "", []

    for letter in w:
        out = alphabet.index(letter) + k
        l.append(alphabet[out])

    return "".join(l)
