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