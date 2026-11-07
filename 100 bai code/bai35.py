m , n = map(int, input().split())
t = 0
t2 = 0
for i in range(m, n + 1):
    t1 = 0
    for j in range(1, round((i+1)**0.5)+1):
        if i % j == 0:
            t1 += 1
    if t1 == 1:
        t+=1
        t2 += i
print(f"{t2/t:.2f}")