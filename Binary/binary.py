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
    return out


def binarydecoder(n):
    string = str(n)
    x = list(string)
    out = []
    for y in range(0, len(x)):
        if x[y] == 1:
            out.append(2 ** (len(x) - y - 1))
    return "".join(out)


print(binarydecoder(1101))
