m , n = map(int, input().split())
for i in range(m, n + 1):
    t1 = 0
    for j in range(1, round((i+1)**0.5)+1):
        if i % j == 0:
            t1 += 1
    if t1 == 1:
        print(i, end=" ")