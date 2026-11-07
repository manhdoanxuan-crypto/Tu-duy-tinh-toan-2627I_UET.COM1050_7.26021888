n = int(input())
a = []
t = 0
for i in range(n):
    val = map(float, input().split())
    a.append(val)
    t+= val[i]
print(t)