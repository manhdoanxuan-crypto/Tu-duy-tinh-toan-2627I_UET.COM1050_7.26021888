n = int(input())
a = []
t = 0
for i in range(n):
    val = map(float, input().split())
    a.append(list(val))
    t=t+int(a[i])
    print(t)
