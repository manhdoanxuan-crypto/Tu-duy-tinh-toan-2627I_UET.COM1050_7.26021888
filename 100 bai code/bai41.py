n = int(input())
a = []
t = 0
for i in range(1, n + 1):
    a.append(float(input()))
    t+= a[i - 1]
print(t)