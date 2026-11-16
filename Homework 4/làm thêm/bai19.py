A = int(input())
f1, f2 = 1, 1
while f1 + f2 <= A:
    f1, f2 = f2, f1 + f2
print(f2)
