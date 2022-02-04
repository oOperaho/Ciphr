def vigenereencoder(w, k):
    k = list(k)
    if len(w) == len(k):
        return "".join(k)
    elif len(w) < len(k):
        return "Word has to be larger than key!"
    else:
        for x in range(len(w) - len(k)):
            k.append(k[x % len(k)])
        return "".join(k)

