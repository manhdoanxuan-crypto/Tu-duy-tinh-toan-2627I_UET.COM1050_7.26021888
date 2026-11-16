def gt(n):
    t = 1
    for i in range(n+1):
        t = t*i
    return t

def tong(k,n):
    m = gt(n)/(gt(k)*gt(n-k))
    return m

n = int(input())
t = 0
for i in range (n):
    a, b = map(int,input().split())
    t += tong(a,b)
print(t)