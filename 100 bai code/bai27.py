n = int(input())
t = 0
for i in range(1, n+1):
    if i% 3 == 0 or i% 5 == 0:
        t+=i
print(t)