import math

def tong_uoc(n):
    if n <= 1:
        return 0
    t = 1
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            t += i
            if i != n // i:
                t += n // i
    return t

a = int(input())
b = int(input())

if a != b and tong_uoc(a) == b and tong_uoc(b) == a:
    print("true")
else:
    print("false")
