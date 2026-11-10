n = int(input())
a = list(map(int, input().split()))
t = 0
for i in range(n):
    if a[i] %2 == 0:
        t+=a[i]
print(t)