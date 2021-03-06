def morsecode(w):
    morse = {"a": "·− ", "b": "−··· ", "c": "−·−· ", "d": "−·· ", "e": "· ", "f": "··−· ", "g": "−−· ", "h": "···· ",
             "i": "·· ",
             "j": "·−−− ",
             "k": "−·− ", "l": "·−·· ", "m": "−− ", "n": "−· ", "o": "−−− ", "p": "·−−· ", "q": "−−·− ", "r": "·−· ",
             "s": "··· ",
             "t": "− ",
             "u": "··− ", "v": "···− ", "w": "·−− ", "x": "−··− ", "y": "−·−− ", "z": "−−·· ", "0": "−−−−− ",
             "1": "·−−−− ", "2": "··−−− ", "3": "···−− ", "4": "····− ", "5": "····· ", "6": "−···· ", "7": "−−··· ",
             "8": "−−−·· ", "9": "−−−−· ", " ": "/"}

    lst = []
    for i in w:
        for k, v in morse.items():
            if i == k:
                lst.append(v)
    return "".join(lst)
