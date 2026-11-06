n = int(input())
t = 0
for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        t += 1
print("Yes" if t == 1 else "No")