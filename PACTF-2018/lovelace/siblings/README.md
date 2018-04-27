# Problem
One 4096-bit RSA key is impossible to break, so 20 must be even better! By chaining each encryption together, surely it’s impossible for you to figure out what the message is?

[Data](problem-data.zip)
# Hint
Numbers don’t have siblings, right? What could that mean?
# Writeup
First of all, we are given a bunch of .pem files. There are many tools online that decode these for you, such as [this one](https://www.google.com/search?q=pem+file+decoder&rlz=1C1CHBF_enUS793US793&oq=pem+file+dec&aqs=chrome.0.0j69i57j0l4.5747j0j7&sourceid=chrome&ie=UTF-8). We can use that to get all of the keys in hex.

We are given lots of keys, and we want to factor them. The "siblings" clues suggests that either the keys are the product of two related primes, or that the keys are related to each other. We can easily verify that none of the keys are products of twin primes by adding one to them and taking the square root. Therefore, we conclude that the keys must be related. We can try a basic common-factor attack by taking the GCF of every pair of keys. Sure enough, this works, and we are able to completely factor all of the keys. 

[All Keys Factored](factored.txt)

Now, it's a straightforward matter of [decrypting RSA with the primes](https://crypto.stackexchange.com/questions/19444/rsa-given-q-p-and-e?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa).
