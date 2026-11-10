a = list(map(int, input().split()))
t = 0
bool = False
for i in range (len(a)):
    if a[i] <= 1:
        continue
    else:
        t1 = 0
        for j in range (2, int(a[i]**0.5) + 1):
            if a[i] % j == 0:
                t1+=1
        if t1 == 0:
            bool = True
            print(a[i], end=" ")
            t+=a[i]

if not bool:
    print("-")
else:
    print(f"\n{t}")