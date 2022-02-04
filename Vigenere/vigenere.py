def vigenereencoder(w, k):
    encrypt = []
    for i in range(len(w)):
        x = (ord(w[i]) + ord(k[i])) % 26
        x += ord('A')
        encrypt.append(chr(x))
    return "".join(encrypt)


def vigeneredecoder(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return "".join(orig_text)
