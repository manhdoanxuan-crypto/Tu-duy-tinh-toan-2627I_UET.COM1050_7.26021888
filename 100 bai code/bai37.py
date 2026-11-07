a , b = map(int, input().split())
c = 0
for i in range(min(a,b) , 0, -1):
    if a % i == 0 and b % i == 0:
        c = i
        break
print(f"{a/c}/{b/c}")