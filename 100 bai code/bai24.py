n =int(input())
n = n - n%3
print((n-3)//3+1 if n>=3 else 0)