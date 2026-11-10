n = int(input())
a = []
t = 0
for i in range(n):
    val = list(map(int, input().split()))
    a.append(val)
for i in range(n):
    t += a[i]
print(t)