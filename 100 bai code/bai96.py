def tong(a):
    s = 0
    t = 0
    for i in a:
        if i%2 == 0:
            s+=i
            t+=1
    return s/t

n = int(input())
a = list(map(int,input().split()))
print(f"{tong(a):.2f}")