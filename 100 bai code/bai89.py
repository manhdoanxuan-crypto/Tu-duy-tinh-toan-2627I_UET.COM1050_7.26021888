def gt(n):
    t = 1
    for i in range(1,n+1,1):
        t = t*i
    return t

def tong(n,k):
    m = gt(n)/(gt(k)*gt(n-k))
    return m

n = int(input())
t = 0
for i in range (n):
    a, b = map(int,input().split())
    t += int(tong(a,b))
print(t)