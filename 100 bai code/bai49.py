n = int(input())
a = list(map(int, input().split()))
t = 0
b = -10*18
x = -1
for i in range(n-1, -1, -1):
    if a[i] > b:
        b = a[i]
        x = i
print(b, i)