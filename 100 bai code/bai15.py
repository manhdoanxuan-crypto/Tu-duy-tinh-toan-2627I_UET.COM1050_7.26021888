a , b ,c  = map(float, input().split())
if a + b > c and a + c > b and b + c > a:
    p = (a + b +c)/2
    S = (p*(p -a)*(p- b)*(p - c))**0.5
    print("Day la 3 canh cua tam giac")
    print(f"{(a + b +c):.2f} {S:.1f}")
else:
    print("Day khong la 3 canh cua tam giac")