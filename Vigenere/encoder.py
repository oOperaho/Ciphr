def vigenereencoder(w, k):
    from operator import add

    res, word, letters = "", "", " abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

    if len(w) > len(k):
        nkey = len(w) - len(k)
        if nkey < len(k):
            word = k[:nkey]
            res = k + w
        elif nkey > len(k):
            if len(k) == 1:
                res = k * (nkey + 1)
            elif len(k) == 2:
                res = k * nkey
            else:
                word = k + k[:nkey]
                res = k + w
        else:
            res += k + k

    elif len(w) < len(k):
        nkey = len(k) - len(w)
        word = k[:-nkey]
        res += w

    else:
        res += k

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
