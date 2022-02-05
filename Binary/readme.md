# Binary Code

Not a cipher decryption, but a simple binary to decimal (and vice-versa) base converter. I made what i thought it would be efficient and easy to understand, of course without 
using the .bin() on python.


Basically, to convert Decimal to Binary, the given number has to be divided by two until it can't be reduced more. Every division has a remainder, and this remainder is pretty
much the binary result, but in backwards.

I just used a while to loop through the values of the decimal, and then append all items on a list. Using .sort() to order these items and then
.join to print the result concludes the function. 



Well, the Binary → Decimal part is a little more difficult, but not complex at all. The code is even smaller than the Dec → Bin code.

