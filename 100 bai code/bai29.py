n = int(input())
t = 0
for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        t += 1
print(t*2 if n**0.5 != int(n**0.5) else t*2-1)