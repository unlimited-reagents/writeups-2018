## Problem

Sometimes​‌‌‌​‌‌‌​‌‌​ there‌​​​​‌‌​​​​‌ is ​‌‌‌​‌​​​‌​‌‌‌more ‌‌​‌‌​​‌​‌​‌‌​‌‌​​​‌‌‌​​‌‌​‌‌​​‌​‌​‌​‌‌‌‌‌​‌‌​‌‌​​​‌‌‌​‌​‌​‌‌‌​​‌​​‌‌​‌​‌‌​‌‌‌​​‌‌​‌​‌‌‌‌‌​‌‌​​​‌than ​​‌‌​​‌​‌​‌‌​‌‌meets ‌​​‌‌​​‌​‌​‌‌​​​the ​‌​‌‌‌​‌​​​‌‌​‌​​​​‌​‌‌‌‌‌​‌‌‌eye​‌​​​‌‌​‌​​​​‌‌​​‌​‌​‌​‌‌‌‌‌​‌‌​​‌​‌​‌‌‌‌​​‌​‌‌​​‌​‌.

## Hint

Maybe if you just squint harder…

## Writeup

Since no additional information is provided, we inspect the html of this question to reveal hidden characters:

![alt-text](https://github.com/unlimited-reagents/writeups-2018/raw/master/PACTF-2018/lovelace/third-eye/html.png "spooky")

There are only 2 types of characters so this suggests that they represent 0 and 1. Getting lucky (or trying a second time) we find that `&#8203;` is 0 and `&zwnj;` is 1 to obtain `01110111011010000110000101110100010111110110010101101100011100110110010101011111011011000111010101110010011010110111001101011111011000100110010101101110011001010110000101110100011010000101111101110100011010000110010101011111011001010111100101100101`

Which translates into `what_else_lurks_beneath_the_eye`
