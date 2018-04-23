## Problem

You received this account.rar file, but it is ‘protected’ under a password. Can you break in?

## Hint

Something tells me the user might not be using complex passwords…

## Writeup

You get a password protected rar. The hint claims that the password is really easy to break, so no need to bother with brute forcing/dictionary attack/etc. Working down the list of the 10 most common passwords, `123456` works.

After unarchiving the file, you get a flag-3.txt file, containing the flag: `rgSueiMYehWJSZPZr`
