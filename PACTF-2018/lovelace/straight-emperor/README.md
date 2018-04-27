## Problem
The Emperor says `ny_nx_tsq3_zumnqq_kwtr_mjwj_6879bd959a` – what could it possibly mean? I hear that he ‘encrypts’ numbers now too, something about appending them to the alphabet…
## Hint
Some say he’s an emperor, I say he’s a salad.
## Writeup
So it's pretty clear that this is a Caesar Cipher, from the "Emperor" and the "salad" and the fact that literally every CTF has a 10 point Caesar Cipher question. However, there are numbers too! The problem says that the numbers were appended to the alphabet, so this probably means that the alphabet looks like "abcdefghijklmnopqrstuvwxyz0123456789" instead of the classic "abcdefghijklmnopqrstuvwxyz." We can un-Caesar Cipher this in the usual way (by brute forcing every possible shift). Here's my Python code:

```python
alpha = 'abcdefghijklmnopqrstuvwxyz0123456789'
def shiftone(s):
  toRet = ''
  for c in s:
    if c == '_':
      toRet += c
      continue
    toRet += alpha[(alpha.index(c) + 1) % 36]
  return toRet
def c_shift(s, n):
  sn = s[:]
  for i in range(n):
    sn = shiftone(sn)
  return sn
for i in range(36):
  print(c_shift("ny_nx_tsq3_zumnqq_kwtr_mjwj_6879bd959a", i))
```
And here's the output:
```
ny_nx_tsq3_zumnqq_kwtr_mjwj_6879bd959a
oz_oy_utr4_0vnorr_lxus_nkxk_798acea6ab
p0_pz_vus5_1wopss_myvt_olyl_8a9bdfb7bc
...
gr_gq_mljw_snfgjj_dpmk_fcpc_z102462y23
hs_hr_nmkx_toghkk_eqnl_gdqd_0213573z34
it_is_only_uphill_from_here_1324684045
ju_jt_pomz_vqijmm_gspn_ifsf_2435795156
...
```
Clearly from this output, the flag is 1324684045.
