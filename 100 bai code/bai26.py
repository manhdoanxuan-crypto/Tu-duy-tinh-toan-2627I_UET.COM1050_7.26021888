n = int(input())
n = n - n%15
print((n + 15)*((n-15)//15+1)//2 if n >= 15 else 0)