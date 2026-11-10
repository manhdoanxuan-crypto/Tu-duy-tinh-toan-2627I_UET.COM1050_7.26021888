a = list(map(int, input().split()))
t = 0
bool = False
for i in range (len(a)):
    if a[i] < 0:
        continue
    else:
        for j in range (int(a[i]**0.5) + 1,1,-1):
            if a[i] % j == 0:
                break
            else:
                bool = True
                print(a[i], end=" ")
                t+=a[i]

if not bool:
    print("-")
else:
    print(f"\n{t}")