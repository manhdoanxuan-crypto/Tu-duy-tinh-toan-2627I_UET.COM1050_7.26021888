n = int(input())
a = []
t = 0
for i in range(n):
    a.append(int(input()))
    t+= a[i]
print(t)