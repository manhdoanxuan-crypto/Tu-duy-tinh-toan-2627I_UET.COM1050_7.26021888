def ucln(a,b):
    c = 1
    if a>b:
        a,b=b,a
    if b == 1 or a == 1:
        return 1
    for i in range(a,1,1):
        if b%i == 0 and a%i == 0:
            c=i
            break
    return c
a,b = map(int,input().split())
if a == 0 or b == 0:
    print("-")
else:
    print(f"{a//ucln(a,b)}/{b//ucln(a,b)}")