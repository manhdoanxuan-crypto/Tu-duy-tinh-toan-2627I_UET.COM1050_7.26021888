n = int(input())
if n < 0:
    n = -n
if n == 0:
    print(1)
else:
    t = 0
    while n>0:
        n =n//10
        t+=1
    print(t)