def binaryencoder(n):
    c = n
    b = []

    while c >= 1:
        b.append(c % 2)
        c = c // 2

    l = list(reversed(b))
    out = ""

    for i in l:
        out += str(i) + ""
    return int(out)


def binarydecoder(n):
    x = list(map(str, str(n)))
    z = 0
    for y in range(0, len(x)):
        if x[y] == "1":
            z += 2 ** (len(x) - y - 1)
    return z
