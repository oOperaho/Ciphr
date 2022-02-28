# Caesar Cipher

This cryptography is pretty simple, and it requires nothing but the positioning of the numbers on the alphabet. All you need is a word/sentence, and a number as a key. 

For example, if you want to hide the word "orange", and you choose 3 as a key, you have to go through each letter of the word, adding 3 positions on the alphabet. So, the
"O on "orange" will be replaced by "R". The decode process does the same thing, but it subtracts the value of the letter. So:

## Encode = Word{Letter} + Key{Letter}
## Decode = Word{Letter} - Key{Letter}

In this case, the word "orange" is now "rudqjh". [I made a article about this cipher, in specific.](https://medium.com/@Operaho/make-a-caesars-cipher-with-python-8958ffa1e90d) 

![image](https://user-images.githubusercontent.com/61850743/150044956-31495810-6a10-4d07-8743-cb946abd5119.png)
