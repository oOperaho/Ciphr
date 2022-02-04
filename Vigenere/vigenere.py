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


def vigenereencoder(w, k):
    encrypt = []
    for i in range(len(w)):
        x = (ord(w[i]) + ord(k[i])) % 26
        x += ord('A')
        encrypt.append(chr(x))
    return "".join(encrypt)
