a = int(input())
b = 0
while a > 0:
    b += a % 10
    a //= 10
print(b%10)
print("May man " if b%10 == 9 else "Chua may man")