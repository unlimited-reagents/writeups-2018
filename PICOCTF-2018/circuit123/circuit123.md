## Problem

Can you crack the key to `decrypt` `map2` for us? The key to `map1` is 11443513758266689915.

## Hint

Have you heard of z3?

## Writeup

Reading the `decrypt.py` that is provided, we see that the single passed in argument (`sys.argv[1]`) is sent into verify as `x` and then used only once in the creation of the array `b` as `[(x >> i) & 1 for i in range(length)]`. This is a familiar statement and we can quickly note that `b[i] = "is the ith bit of x set?"`. This essentially means that we need to find the initial `length` booleans need to be set properly for us to pass verify() (64 in the case of map1 and 128 in the case of map2).

After some more inspection we learn that all this code is doing is reading in gate x as either the `or` or `xor` of two previously defined gates (with some of these 2 inputs being negated). The final goal is to get gate `check[0]` to output `check[1]`, so we can see right away that this is a constraint satisfiability challenge.

As the hint notes, we will make use of z3, Microsoft's theorem prover. All we need to do is to set up our constraints as Bools and then let z3 do its thing. Luckily, the decryption tool provides us with easy input that we can poach and modify ever so slightly.

First we open our desired file (map2 for the flag) and read the cipertext, gates list, and desired output check.
```python
from z3 import *
from tqdm import *

f = open("map2.txt",'r')
cipher, chalbox = eval(f.read())
length, gates, check = chalbox
```

Next we instantiate our solver and give it 128 (or 64 for map1) variables to try to solve for.

```python
s = Solver()

b = [Bool(i) for i in range(length)]
```

Now we steal the input from decrypt.py

```python
for name, args in gates:
    if name == 'true':
        b.append(1)
    else:
        u1 = b[args[0][0]] ^ args[0][1]
        u2 = b[args[1][0]] ^ args[1][1]
        if name == 'or':
            b.append(u1 | u2)
        elif name == 'xor':
            b.append(u1 ^ u2)
return b[check[0]] ^ check[1]
```
Instead of computing u1 and u2 directly, we must instantiate them as new (helper) Bools for z3. 
```python
u1 = Not(b[args[0][0]]) if args[0][1] else b[args[0][0]]
u2 = Not(b[args[1][0]]) if args[1][1] else b[args[1][0]]
```
Similarly, instead of appending to `b`, we will define a new Bool and append that.

```python
b.append(Bool(i+length))
```
Now we feed this new constraint as a function of `u1`, `u2` and output `b[-1]` (this new variable we just appended) into our solver 

```python
if name == 'or':
	s.add(b[-1] == Or(u1,u2))
elif name == 'xor':
	s.add(b[-1] == Xor(u1,u2))
```

Our final code then looks like:

```python
from z3 import *
from tqdm import *

f = open("map2.txt",'r')
cipher, chalbox = eval(f.read())
length, gates, check = chalbox

s = Solver()

b = [Bool(i) for i in range(length)]
for i in tqdm(range(len(gates))):
    name, args = gates[i]
    if name == 'true':
        b.append(True)
    else:
        u1 = Not(b[args[0][0]]) if args[0][1] else b[args[0][0]]
        u2 = Not(b[args[1][0]]) if args[1][1] else b[args[1][0]]

        b.append(Bool(i+length))
        if name == 'or':
        	s.add(b[-1] == Or(u1,u2))
        elif name == 'xor':
        	s.add(b[-1] == Xor(u1,u2))

u = Not(b[check[0]]) if check[1] else b[check[0]]
s.add(u)

s.check()
m = s.model()

ans = 0
for i in range(length):
	ans *= 2
	ans += is_true(m[b[length-i-1]])
	
print ans
```

Running on map1.txt gives the expected result and so we run on map2.txt to get `219465169949186335766963147192904921805` 

And `python3 decrypt.py 219465169949186335766963147192904921805 map2.txt` prints
```
Attempting to decrypt map2.txt...
Congrats the flag for map2.txt is: picoCTF{36cc0cc10d273941c34694abdb21580d__aw350m3_ari7hm37ic__}
```