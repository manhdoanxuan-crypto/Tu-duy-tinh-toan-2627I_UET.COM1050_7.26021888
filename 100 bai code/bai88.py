def ucln(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a

def rut_gon(a, b):
    if b == 0:
        return "-"
    if a == 0:
        return "0"
    if b < 0:
        a = -a
        b = -b
    c = ucln(a, b)
    t = a // c
    m = b // c
    if m == 1:
        return str(t)
    return f"{t}/{m}"

a, b = map(int, input().split())
print(rut_gon(a, b))