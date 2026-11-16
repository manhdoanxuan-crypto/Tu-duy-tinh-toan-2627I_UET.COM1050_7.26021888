n = int(input())
while n > 1 and n % 3 == 0:
    n //= 3
if n == 1:
    print("Co")
else:
    print("Khong")
