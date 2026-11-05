t = int(input())
print(12000 if t == 1 else 12000 + (t-1)*10000 if 2 <= t <= 30 else 12000 + 29*10000 + (t -30)*9000)