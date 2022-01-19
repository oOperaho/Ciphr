word = str(input("Enter the word to encrypt: ")).strip().lower().replace(" ", "")
key = int(input("Enter the key (0-26): "))
alphabet, out, l = " abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", "", []

for letter in word:
    out = alphabet.index(letter) + key
    l.append(alphabet[out])

print("".join(l))
