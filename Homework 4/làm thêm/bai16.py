n = int(input())
c = 0
l = 0

while n > 0:
    a = n % 10
    if a % 2 == 0:
        c += 1
    else:
        l += 1
    n //= 10

print(c,l)
