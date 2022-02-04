def ciphertext(w, k):
    l, c = list(k), 0
    dif = abs(len(w) - len(k))
    while True:
        if len(w) == len(k):
            return "".join(l)
        elif len(w) < len(k):
            "".join(l)
            l = l[:dif]
            return "".join(l)
        else:
            l.append(k[c])
            if len(l) == len(w):
                break
            c += 1


print(ciphertext("banana", "oi"))
