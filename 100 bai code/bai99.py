import math

def cp(a):
    if a < 0:
        return 0
    b = int(math.sqrt(a))
    if b*b == a:
        return 1
    else:
        return 0

a = list(map(int,input().split()))
s = 0
t = 0
for i in (len(a)):
    if cp(a[i]) == 1:
        s+=a[i]
        t+=1
if t == 0:
    print("-")
else:
    print(f"{s/t:.1f}")