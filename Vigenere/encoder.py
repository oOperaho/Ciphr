def vigenereencoder(w, k):
    kl = len(k)
    key_index, word_index = [], []
    encrypt = ""
    for x in k:
        key_index = ord(x)
    for y in w:
        word_index = ord(y)

    for i in range(len(word_index)):
        c = (word_index[i] + key_index[i % kl]) % 26
        encrypt += chr(c + 65)

    return encrypt


def vigeneredecoder(w, k):
    kl = len(k)
    key_index, word_index = [], []
    decrypt = ""
    for x in k:
        key_index = ord(x)
    for y in w:
        word_index = ord(y)

    for i in range(len(word_index)):
        c = (word_index[i] + key_index[i % kl]) % 26
        decrypt += chr(c + 65)

    return decrypt
