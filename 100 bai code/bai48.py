n = int(input())
a = list(map(int, input().split()))
t = 0
bool = False
for i in range(n):
    if a[i] % 5 == 0:
        bool = True
        print(a[i], end= " ")
        t+= a[i]
if not bool:
    print("-")
else:
    print(t)