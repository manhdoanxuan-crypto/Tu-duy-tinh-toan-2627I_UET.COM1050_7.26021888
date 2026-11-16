import math

a = int(input())
b = int(math.sqrt(a))
if b*b == a:
    print(f"{a} là số chính phương.")
else:
    print(f"{a} không phải là số chính phương.")
