a , b ,c  = map(float, input().split())
if a + b > c and a + c > b and b + c > a:
    p = (a + b +c)/2
    S = (p*(p -a)*(p- b)*(p - c))**0.5
    print("Dien tich tam giac =" , S)
else:
    print("khong là tam giac")