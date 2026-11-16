def cv(a,b,c):
    cv = a+b+c
    return cv
def dt(a,b,c):
    p = (a+b+c)/2
    S = (p*(p-a)*(p-b)*(p-c)**0.5)/2
    return S
a,b,c= map(float,input().split())
print(f"{cv:.1f} {dt:.3f}")
