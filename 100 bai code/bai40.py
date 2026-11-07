
import math

k = int(input())
t = 0
for i in range(0, 10**18):
    a = math.trunc(i**0.5)
    if a**2 == i:
        print(i , end = " ")
        t+=1
    if t == k:
        break