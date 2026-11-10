n = int(input())
a = list(map(int, input().split()))
t = 0
for i in range(n):
    if i%2 == 1:
        t+=a[i]
print(t)