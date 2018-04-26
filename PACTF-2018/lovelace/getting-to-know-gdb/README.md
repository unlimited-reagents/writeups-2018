## Problem

A friend sent me a [mysterious binary](https://github.com/unlimited-reagents/writeups-2018/raw/master/PACTF-2018/lovelace/getting-to-know-gdb/mysterious) mysterious binary. It’s supposed to print out the flag, but it’s giving me a weird poem and some hex instead.

## Hint

The flag is in there somewhere, but something gives me the feeling that searching the binary for strings wont help…

## Writeup

Running the file we get some arbitrary base64 that doesn't translate into anything useful, so we can disregard this output and look into the assembly itself. 

A nice place to start is always the main, so we run `gdb mysterious` and then `disass main`, 

![alt-text](https://github.com/unlimited-reagents/writeups-2018/raw/master/PACTF-2018/lovelace/getting-to-know-gdb/disass_main.png "main")

but this yeilds nothing of interest as this was likely compiled with g++ so the main is not really the main but rather just something that calls it.

We then go to the next best place, the loop running the prints. To get here we just run the binary with `r` and click `Ctrl+C` during the execution (not on any sort of timer since the binary runs forever). If you're using stock gdb you would then use `where` to get a trace of the called functions, but pwndbg does this for us. 

![alt-text](https://github.com/unlimited-reagents/writeups-2018/raw/master/PACTF-2018/lovelace/getting-to-know-gdb/paused.png "paused execution")

We can see that we're in `std::thread::sleep::heee2828c335b094d` which is of no interest to us, but this function was called by `binary::main::hf421c7ec894951b1` which seems promising! [Disassemblying](https://github.com/unlimited-reagents/writeups-2018/raw/master/PACTF-2018/lovelace/getting-to-know-gdb/disassembly.txt) this new function gives a whole lot of assembly, which we can throw into our favorite text editor to analyize. Right off the bat the thing we're interested in is printing, so we search for "print" in the disassembly and find calls to `_ZN3std2io5stdio6_print17ha2600cbffab86873E`. The last of these is probably the one we want, which is at `0x0000555555559c8e`.

![alt-text](https://github.com/unlimited-reagents/writeups-2018/raw/master/PACTF-2018/lovelace/getting-to-know-gdb/actual_main.png "actual main")

Setting a breakpoint here with `b *0x0000555555559c8e` we continue execution with `c` and instantly hit the breakpoint.

![alt-text](https://github.com/unlimited-reagents/writeups-2018/raw/master/PACTF-2018/lovelace/getting-to-know-gdb/breakpoint.png "breakpoint")

If we run `c` a few more times, we can note that there seems to be a suspicious string at `0x5555557898b0` that looks a lot like the printed base64. Digging around for strings around this memory with `x /40s 0x5555557898b0-0x50` we find our flag `why_use_breakpoints_if_you_have_good_timing`.

![alt-text](https://github.com/unlimited-reagents/writeups-2018/raw/master/PACTF-2018/lovelace/getting-to-know-gdb/strings.png "strings")

Alternatively, if we didn't have the magic of pwndbg, we could see that this location is significant because right before the call to print, some shuffling occurs with the r13, rbp, rdi, and r13 registers. We examine the location of these, and `x $r13` tells us that r13 is at `0x7fffffffdab0`. Searching around a bit we find that nearby (at `0x7fffffffdad0`) we have another address (`0x7fffffffdb50`) which itself has another address (`0x7fffffffdaf0`) which has something resembling a heap address at it (`0x5555557898b0`) which has the suspicious string. 
In short, you should use pwndbg :p