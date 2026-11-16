n = int(input())
t = 0
if n == 0:
    print(1)
elif n < 0:
    n = -n
else:
    while n:
        n = n%10
        n =n//10
        t+=1
    print(t)