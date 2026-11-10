n = int(input())
t = 0
a = list(map(int, input().split()))
for i in range(n):
    t += a[i]
print(t)