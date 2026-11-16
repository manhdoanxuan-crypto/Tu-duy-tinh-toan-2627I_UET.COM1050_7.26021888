def ucln(a,b):
    c = -10*18
    if a == 0 or b == 0:
        return "-"
    else:
        if a>b:
            a,b=b,a
        for i in range(a,1,-1):
            if b%i == 0 and a%i == 0:
                c=i
                break
        return c
a,b = map(int,input().split())
print(f"{a//ucln(a,b)}/{b//ucln(a,b)}")