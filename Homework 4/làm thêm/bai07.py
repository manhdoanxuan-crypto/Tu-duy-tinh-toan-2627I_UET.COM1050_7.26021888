a = int(input())
t = 0
for i in range(1, a + 1):
    if a % i == 0:
        t += 1
print(t)
