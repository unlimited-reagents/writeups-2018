## Problem

The solution to this problem lies within the Chromium source code. Literally. There is some string in there that mentions a flag and PACTF…

## Hint

This problem builds off of a similarly named problem in PACTF 2017.

## Writeup

I have mental issues so I did this in a really AIDS way, but it still worked!

Remembering what I did last year for this problem, I tried searching through all the online Chromium source repos but couldn't find anything, so I gave up and decided to run a search locally.

I followed these directions to download the Chromium source: <https://www.chromium.org/developers/how-tos/get-the-code> and searched through the source with `grep -rnw './' -i -e 'pactf'`, yielding the flag `pactf-flag-4boxdpa21ogonzkcrs9p.com` in `net/http/transport_security_state_static.json`.
