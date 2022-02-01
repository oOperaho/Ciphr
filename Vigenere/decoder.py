def vigeneredecoder(w, k):
    from operator import sub

    res, word, letters, srettel = "", "", " abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz ", " zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba "

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
        w = k[:-nkey]
        res += w

    else:
        res += k

    s, l, fin, enc = [], [], [], []

    for i in w:
        s.append(letters.find(i))

    for j in res:
        l.append(letters.find(j))

    for n in range(0, len(s)):
        s[n] = s[n] + 1

    fin = list(map(sub, s, l))

    for x in fin:
        if x < 0:
            x = abs(x) + 1
            enc.append(srettel[x])
        else:
            enc.append(letters[x])

    return "".join(enc)
