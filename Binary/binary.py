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

#
# def binarydecoder(n):
