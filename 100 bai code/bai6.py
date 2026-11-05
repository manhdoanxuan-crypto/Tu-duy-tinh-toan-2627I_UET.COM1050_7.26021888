a , b, c = map(int, input().split())
p = (a + b + c)/2
print(f"{(a + b + c):.1f} {(p*(p-a)*(p-b)*(p-c))**0.5:.3f}")