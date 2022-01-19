from operator import sub

word = str(input("Type the word to be decrypted: ")).strip().lower().replace(" ", "")
key = str(input("Type the vigenere key: ")).strip().lower().replace(" ", "")
nkey = 0
res, w, letters, srettel = "", "", " abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", " zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba"

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

print("".join(enc))
