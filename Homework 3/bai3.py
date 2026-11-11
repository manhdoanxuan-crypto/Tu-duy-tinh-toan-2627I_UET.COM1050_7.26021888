a, b, c = map(float, input().split())
if a > b:
  a, b = b, a
if a > c:
  a, c = c, a
if b > c:
  b, c = c, b
if a+ b > c and a+c > b and b + c > a:
    if a == b == c:
        print("Tam giac deu")
    elif a == b or b == c or c == a and a**2 + b**2 != c**2:
        print("Tam giac can")
    elif a**2 + b**2 == c**2:
       print("Tam giac vuong")
    else:
       print("Tam giac thuong")
print()
p =(a+b+c)/2
print(a+b+c, (p*(p-a)*(p-b)*(p-c))**0.5)