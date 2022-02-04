def vigenereencoder(w, k):
    encrypt = []
    for i in range(len(w)):
        x = (ord(w[i]) + ord(k[i])) % 26
        x += ord('a')
        encrypt.append(chr(x))
    return "".join(encrypt)


def vigeneredecoder(w, k):
    decrypt = []
    for i in range(len(w)):
        x = (ord(w[i]) - ord(k[i]) + 26) % 26
        x += ord('a')
        decrypt.append(chr(x))
    return "".join(decrypt)
