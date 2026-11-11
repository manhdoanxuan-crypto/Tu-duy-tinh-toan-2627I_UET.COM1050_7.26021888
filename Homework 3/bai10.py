x0, y0 = map(float,input().split())
R = float(input())
x1, y1 = map(float,input().split())
print(f"A{x1,y1} nam tren duong tron" if (x1-x0)**2 + (y1-y0)**2 == R**2 else f"A{x1,y1} nam ngoai duong tron" if (x1-x0)**2 + (y1-y0)**2 > R**2 else f"A{x1,y1} nam trong duong tron" )