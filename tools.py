import re


def newKey(w, k):
    k = list(k)
    if len(w) == len(k):
        return k
    else:
        for i in range(len(w) - len(k)):
            k.append(k[i % len(k)])
    return "".join(k)


def process_text(text):
    new_text = re.sub("[^A-Za-z\s]", "", text)
    return new_text


def process_int(num):
    new_int = re.sub("[^0-9]", "0", num)
    return new_int
