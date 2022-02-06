# Binary Code

Not a cipher decryption, but a simple binary to decimal (and vice-versa) base converter. I made what i thought it would be efficient and easy to understand, of course without 
using the .bin() on python.


Basically, to convert Decimal to Binary, the given number has to be divided by two until it can't be reduced more. Every division has a remainder, and this remainder is pretty
much the binary result, but in backwards.

I just used a while to loop through the values of the decimal, and then append all items on a list. Using .sort() to order these items and then
.join to print the result concludes the function. 

### 12 → 12 / 2 = **6**, res: 0  |  6 / 2 = **3**, res: 0  |  3 / 2 = **1**, res: 1  |  1 / 1 = **1**  |  ← Reverse this
### Result: 1100

Well, the Binary → Decimal part is a little more difficult, but not complex at all. The code is even smaller than the Dec → Bin one. Given the binary, it can be simple converted
in that way:

Every digit (bit) has its position, so you can pick the number (0 or 1) and multiply it by 2 to the power of the position of the digit _backwards_. Then you add the results to get your decimal. It is also important to say that the position of the number starts with 0.

### 1101 → 1 x 2³ = 8  |  1 x 2² = 4  |  0 x 2¹ = 0  |  1 x 2º = 1  
### Result: 8 + 4 + 0 + 1 = **13**

