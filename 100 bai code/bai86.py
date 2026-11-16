def cv(a,b,c):
    cv = float(a+b+c)
    return cv
def dt(a,b,c):
    p = (a+b+c)/2.0
    S = (p*(p-a)*(p-b)*(p-c))**0.5
    return S
a,b,c= map(float,input().split())
print(f"{cv(a,b,c):.1f} {dt(a,b,c):.3f}")
