## Problem

As the `song` draws closer to the end, another executable `be-quick-or-be-dead-3` suddenly pops up. This one requires even faster machines. Can you run it fast enough too? You can also find the executable in /problems/be-quick-or-be-dead-3_0_fa64b8365f5d2ac445b925be0960b943.

## Hint

How do you speed up a very repetitive computation?

## Writeup

If we disassembly the binary we find that it has the same format as previous be-quick-or-be-dead challenges:

```c++
header(*(_QWORD *)&argc, argv, envp);
set_timer(*(_QWORD *)&argc);
get_key(*(_QWORD *)&argc);
print_flag(*(_QWORD *)&argc);
```
We only really care about `get_key()` and so looking at that we find that it calls `calculate_key()` and this in turn just does:

```c++
return calc(0x18E9Fu);
```

After traversing all of these layers we finally get that `calc()` is defined as 

```c++
__int64 __fastcall calc(unsigned int a1)
{
  int v1; // ebx@3
  int v2; // ebx@3
  int v3; // er12@3
  int v4; // ebx@3
  int v6; // [sp+1Ch] [bp-14h]@2

  if ( a1 > 4 )
  {
    v1 = calc(a1 - 1);
    v2 = v1 - calc(a1 - 2);
    v3 = calc(a1 - 3);
    v4 = v3 - calc(a1 - 4) + v2;
    v6 = v4 + 4660 * calc(a1 - 5);
  }
  else
  {
    v6 = a1 * a1 + 9029;
  }
  return (unsigned int)v6;
}
```

Anyone experienced with programming will see the flaw in calculating this way as `calc(10)` is called [the number of times we can represent x-10 as the sum of arbitrary 1,2,3,4, or 5s] for `calc(x)` which grows much to fast for us to call it with argument 0x18E9F (~100,000). Luckily, this repetition can be avoided with dynamic programming.

I was too lazy to unroll this into dp, so I decided to just implement memoization (requiring the addition of just 2.5 lines) to get:

```c++
unordered_map<unsigned int,unsigned int> memo;      // addition
__int64 __fastcall calc(unsigned int a1)
{
  if (memo.find(a1) != memo.end()) return memo[a1]; // addition
  int v1; // ebx@3
  int v2; // ebx@3
  int v3; // er12@3
  int v4; // ebx@3
  int v6; // [sp+1Ch] [bp-14h]@2

  if ( a1 > 4 )
  {
    v1 = calc(a1 - 1);
    v2 = v1 - calc(a1 - 2);
    v3 = calc(a1 - 3);
    v4 = v3 - calc(a1 - 4) + v2;
    v6 = v4 + 4660 * calc(a1 - 5);
  }
  else
  {
    v6 = a1 * a1 + 9029;
  }
  return memo[a1] = (unsigned int)v6;               // modification
}
```

Running `calc(0x18E9F)` yields `3610015907` in just 0.3 sec.

Now all we have to do is skip over calculate_flag and set the result directly to 3610015907. We can achieve this by opening the binary in GDB and jumping past `get_key()`

![alt-text](https://github.com/unlimited-reagents/writeups-2018/raw/master/PICOCTF-2018/be-quick-or-be-dead-3/main.png "main")

From here we run with `r` and let it hit the first breakpoint. Once it does, we execute `jump *0x04008d` to skip over `get_key()`. Examining the get key function, we see that the key is stored at `0x6010b0` so we can run `set *0x6010b0 = 3610015907` to put the desired value in key.

![alt-text](https://github.com/unlimited-reagents/writeups-2018/raw/master/PICOCTF-2018/be-quick-or-be-dead-3/get_key.png "main")

Continuing with `c` gives us the flag.

![alt-text](https://github.com/unlimited-reagents/writeups-2018/raw/master/PICOCTF-2018/be-quick-or-be-dead-3/flag.png "main")


`picoCTF{dynamic_pr0gramming_ftw_1ffc009d}`