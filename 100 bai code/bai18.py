a , b = map(int, input().split())
if b % 400 == 0 or (b % 4 == 0 and b % 100 != 0):
    if a == 2:
        print(29)
    elif a in [1 , 3 , 5 , 7 , 8 , 10 , 12]:
        print(31)
    else:
        print(30)
else:
    if a == 2:
        print(28)
    elif a in [1 , 3 , 5 , 7 , 8 , 10 , 12]:
        print(31)
    else:
        print(30)