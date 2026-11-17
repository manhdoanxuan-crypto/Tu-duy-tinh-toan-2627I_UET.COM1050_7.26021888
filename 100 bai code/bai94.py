def ucln(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

def bcnn(a,b):
    return (a*b)//ucln(a,b)

def rutgon(a,b):
    if ucln(a,b) != 1:
        return a//ucln(a,b),b //ucln(a,b)
    else:
        return a,b

def cong(a,b,c,d):
    e = int((bcnn(b,d)/b)*a)
    f = int((bcnn(b,d)/d)*c)
    if (e+f)//bcnn(b,d) >= 1 or (e+f)//bcnn(b,d) <= -1:
        g,h = rutgon((e+f),bcnn(b,d))
        return f"{g//h},{g%h}/{h}"
    else:
        g,h = rutgon((e+f),bcnn(b,d))
        return f"{g}/{h}"

def tru(a,b,c,d):
    e = int((bcnn(b,d)/b)*a)
    f = int((bcnn(b,d)/d)*c)
    if (e-f)//bcnn(b,d) >= 1:
        g,h = rutgon((e-f),bcnn(b,d))
        return f"{g//h},{g%h}/{h}"
    else:
        g,h = rutgon((e-f),bcnn(b,d))
        return f"{g}/{h}"
def nhan(a,b,c,d):
    e = a*c
    f = b*d
    e, f = rutgon(e,f)
    if e//f >= 1 or e//f <=-1:
        return f"{e//f},{e%f}/{f}"
    else:
        return f"{e}/{f}"

def chia(a,b,c,d):
    return nhan(a,b,d,c)
a,b = map(int,input().split())
c,d = map(int,input().split())
print(cong(a,b,c,d))
print(tru(a,b,c,d))
print(nhan(a,b,c,d))
print(chia(a,b,c,d))