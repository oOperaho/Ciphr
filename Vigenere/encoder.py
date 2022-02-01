def vigenereencoder(w, k):
    from operator import add

    nkey = 0
    res, w, letters = "", "", " abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

    if len(word) > len(key):
        nkey = len(word) - len(key)
        if nkey < len(key):
            w = key[:nkey]
            res = key + w
        elif nkey > len(key):
            if len(key) == 1:
                res = key * (nkey + 1)
            elif len(key) == 2:
                res = key * nkey
            else:
                w = key + key[:nkey]
                res = key + w
        else:
            res += key + key

    elif len(word) < len(key):
        nkey = len(key) - len(word)
        w = key[:-nkey]
        res += w

    else:
        res += key

    s, l, fin, enc = [], [], [], []

    for i in word:
        s.append(letters.find(i))

    for n in range(0, len(s)):
        s[n] = s[n] - 1

    for j in res:
        l.append(letters.find(j))

    fin = list(map(add, s, l))

    for x in fin:
        enc.append(letters[x])

    return "".join(enc)
