# Go Git It (25 Points)

## Problem

The code samurai (also known by his pseudonym Nicholas) was making some final optimizations on his program when… he accidentally decapitated it.

Download the samurai’s repository: go git it.tar.bz2

## Hint

Perhaps ‘chopping a branch off a tree’ would be the more precise analogy.

## Writeup

Extracting the downloaded bzip yields a folder called WaveFunctionCollapse. `ls -a` indeed verifies that the directory is a git repository. Based on the hint and problem statement, it is implied that somehow, some commit has become HEADless.

Therefore, it would be great if we could look at all commits and find one that is out of place, which we can do with `git reflog |  awk '{ print $1 }' | xargs gitk`.

We can find a commit titled I AM THE CODE SAMURAI, containing the flag `3x3rc1z3_caut10n_wh3n_d3tach1ng_ur_h3ad`.

![alt-text](https://github.com/unlimited-reagents/writeups-2018/raw/master/PACTF-2018/lovelace/go-git-it/gitk.png "3x3rc1z3_caut10n_wh3n_d3tach1ng_ur_h3ad") 
