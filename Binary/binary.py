def binaryencoder(n):
    if n == 0:
        return 0
    c, b = n, []

    while c >= 1:
        b.append(c % 2)
        c = c // 2

    l, out = list(reversed(b)), ""

    for i in l:
        out += str(i) + ""
    return int(out)


def binarydecoder(n):
    if n == 0:
        return 0
    x = list(map(str, str(n)))
    out = 0
    for y in range(0, len(x)):
        if x[y] == "1":
            out += 2 ** (len(x) - y - 1)
    return out
