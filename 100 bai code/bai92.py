def cong(a,b):
    return a+b
def chia(a,b):
    return a/b
a,b,c = map(int,input().split())
print(f"{cong(a,cong(b,c))} {cong(chia(a,b),c):.2f} {chia(a,cong(b,c)):.3f}")