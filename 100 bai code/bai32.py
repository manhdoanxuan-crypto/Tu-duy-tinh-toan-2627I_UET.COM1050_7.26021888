m ,n = map(int, input().split())
t1 = 0
t2 = 0
for i in range(m, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        t1 += 1
    if i % 2 == 0:
        t2 += i
print(f"{t1} {t2}")