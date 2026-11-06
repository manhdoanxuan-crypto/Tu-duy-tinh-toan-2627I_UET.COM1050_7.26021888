n = int(input())
n = n - n%2
print((n+2)*((n-2)//2+1)//2 if n >= 2 else 0)