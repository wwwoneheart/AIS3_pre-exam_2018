#!/usr/bin/env python3
import os
import random

with open('flag-encrypted', 'rb') as data:
    cipher = data.read().strip()

a = []
ex = b'AIS3{'

cipher = [x for x in bytes(cipher)]
c = 0
k = []
for i in range(5):
    a.append(cipher[i]^ex[i])
for j in range(6,1,-1):
    a.append(cipher[len(cipher)-j]^a[len(a)-1])
    c += 1
g = 0
for i in range(len(cipher)):
    k.append(cipher[i]^a[g])
    g += 1
    if g >= len(a):
        g = 0
ans = ""
for j in range(len(k)):
    ans += chr(k[j])
print(ans)
