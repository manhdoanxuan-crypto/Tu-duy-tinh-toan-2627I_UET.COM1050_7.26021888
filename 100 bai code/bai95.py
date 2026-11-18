def tong(a):
    s = 0
    for i in a:
        s+=i
    return s

n = int(input())
a = list(map(int,input().split()))
print(f"{tong(a)/n:.1f}")