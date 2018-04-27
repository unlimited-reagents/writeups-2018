# Problem
We intercepted this message, but we can�t make heads or tails of it. It was rattled off so fast, too� How could anyone be that good at using a cipher?

Anyway, here�s the message. Good luck!
`Tazhii, Li�i�', Dzeeh Ma'ii, Dib� y�zh�, W�l�ch��', Tl'�z� Tin, Dib� M�s�, Li�i�', Dzeeh, Dib�, Tazhii, Dzeeh, Gah, Neeshch'��', Dzeeh, B��sh dootl'izh`
# Hint
This definitely doesn�t look like English. What else could it be? Perhaps looking through the history books might help�
# Writeup
Googling some of the words, we see that they are Navajo for some animals. It's pretty well known that Navajo code talkers were used in WWI to convey messages (or be like me and read [this xkcd comic](https://xkcd.com/257/)).
There's a handy table of words to letters [here](https://en.wikipedia.org/wiki/Code_talker#Navajo_code_talkers). We can use this to translate the message, and get the flag.

Translating the message, we get `THEFLAGISCHESTERNEZ`, meaning that the flag is `chesternez`.