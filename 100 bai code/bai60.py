import math

a = list(map(int, input().split()))
bool = False
t = 0
t1 = 0
for i in range (len(a)):
    if i > 0:
        b = math.trunc(i**0.5)
        if b**2 == i:
            t +=a[i]
            t1 +=1
            bool = True
if bool == False:
    print("-")
else:
    print(f"{(t/t1):.1f}")