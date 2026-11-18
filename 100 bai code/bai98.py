def nt(a):
    t = 0
    if a <=1:
        return 0
    elif a == 2 or a == 3:
        return 1
    else:
        for i in range(2,int(a**0.5+1),1):
            if a%i == 0:
                t+=1
        if t == 0:
            return 1
        else:
            return 0

a = list(map(int,input().split()))
s = 0
t = 0
for i in range (len(a)):
    if nt(a[i]) == 1:
        s+=a[i]
        t+=1
if t == 0:
    print("-")
else:
    print(f"{s/t:.2f}")