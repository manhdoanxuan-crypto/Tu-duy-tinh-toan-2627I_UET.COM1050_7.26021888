a, b , m = map(float, input().split())
c, d , n = map(float, input().split())
D = a * d - b * c
Dx = m * d - b * n
Dy = a * n - m * c
if D != 0:
    x = Dx / D
    y = Dy / D
    print(f"x = {x}")
    print(f"y = {y}")
else:
    if Dx == 0 and Dy == 0:
        print("Vo so nghiem")
    else:
        print("vo nghiem")
