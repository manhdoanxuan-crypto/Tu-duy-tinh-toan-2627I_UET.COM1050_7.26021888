n = int(input())
a = list(map(int, input().split()))
t = 0
for i in range(n):
    if a[i]> 0:
        t+=1
print(t)