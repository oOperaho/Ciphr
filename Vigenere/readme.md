# Vigenere Cipher

This is my take on the classic Vigenere encoder/decoder. The challenge was, make a encoder for this cipher without googling anything of it. This is one of the final results.

So, the way i thought it would be simple and "easy" to understand involves some list management and a little bit of work around with the strings and outputs. The python code is really self-explanatory, but i'll describe the logic behind it. 
Basically, the Vigenere cipher uses the Vigenere Grid, which is a 26x26 table, with the alphabet in loop. 

![image](https://user-images.githubusercontent.com/61850743/149991107-134fe95d-7977-47d1-a973-7ec2a15b8e2b.png)

## Encoding

To encrypt a word/sentence, you need to use a key (which is another word, or sentence), and repeat that key in order to complete the size of the word you want to encrypt. For example, if you want to encode the word "_Python_" with the key "_Sun_", you'll repeat Sun until it's the size of Python (sunsun).

Then you have to look at the Vigenere Grid, and find the letter that corresponds to the intersection between the letters in the key and the main word.

In that case, if you look at the image, the first letter of the main word "P", has to intersect with the first letter of the key, "S", which is "H", then you continue with the rest. 
To put this in a python script, i had to think in a way to find the numeric expression on the vigerene cipher, and this part was pretty easy, since the table kind of explains what's going on there. I found that if you add the number s of the letters and then subtract the result by 1, you'll have the correct encoded letter. For example, "B" + "I": 
You replace the letter with its numbers on the AIZ26 method (B = 2 and I = 9), and you have 11. Subtract 1 of this, and you got 10, or J, in the alphabet.  
If you look  at the Grid, you'll see the same result. So:

### Encode = Word{Letter} + Key{Letter} - 1

You may note that this only works for some letters. If you add O with O, you'll have 30, which is greater than 26. To solve this, the UI has a regex to provides numbers that are greater than 26.

## Decoding

This part is a little bit different, because the notation changes, but it's not that hard. You just need to move between the alphabet in other way, replacing the orientation of
the letters.
The expression of the decode i made uses the pattern _"zyxwvutsrqponmlkjihgfedcbaabcdefghijklmnopqrstuvwxyz"_. This can be more understandable in the code, but here i'll show how to do it.

You still need to use the previous formula, but replacing the -1 with +1. Then, you have to find the corresponding letter on another string, which is " zyxwvutsrqponmlkjihgfedcba" on the code. This way, you can apply the method of adding 1 to the counting without tresspassing the alphabet limit.

### Decode = Word{Letter} + Key{Letter} + 1
