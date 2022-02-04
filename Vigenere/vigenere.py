def ciphertext(w, k):
    key = list(k)
    if len(w) == len(key):
        return key
    elif len(w) < len(k):
        return "".join(k[:len(w)])
    else:
        for i in range(len(w) - len(key)):
            key.append(key[i % len(key)])
    return "" . join(key)



