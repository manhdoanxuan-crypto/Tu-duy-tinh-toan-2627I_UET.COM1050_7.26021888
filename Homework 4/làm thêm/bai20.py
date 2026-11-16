n = int(input())
d = 0
while n > 0:
    a = n % 10
    if a in (2, 3, 5, 7):
        d += 1
    n //= 10
print(d)
