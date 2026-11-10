a = list(map(int, input().split()))
t = 0
bool = False
for i in range (a.len()):
    if a[i] < 0:
        continue
    else:
        for j in range (a[1]**0.5):
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