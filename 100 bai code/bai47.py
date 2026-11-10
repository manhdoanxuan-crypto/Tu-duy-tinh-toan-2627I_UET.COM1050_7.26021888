n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    if a[i] > 0:
        a[i] = a.pop(i)
        b.append(a[i])
print(b)
print(a)