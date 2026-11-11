a, b , c = map(float,input().split())
if a == b == c == 0:
    print("Vo so nghiem")
elif c == 0 and a!= 0 and b!=0:
    print("Vo nghiem")
elif a == 0 and b!=0 :
    print(-c/b)
else:
    delta = -b**2 + 4*a*c
    print((-b + delta**0.5)/(2*a), (-b-delta**0.5)/(2*a))