m , n = map(int, input().split())
t = 0
for i in range(m, n + 1):
    if n % 3 == 0:
        t += 1
print(t)