def tong(x, ak, nk):
    return ak*(x**nk)
k , x = map(int,input().split())
t = 0
for i in range (k):
    ak, nk = map(int,input().split())
    t += tong(x,ak,nk)
print(t)