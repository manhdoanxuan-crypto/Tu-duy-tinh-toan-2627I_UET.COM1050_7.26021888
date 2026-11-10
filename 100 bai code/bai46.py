n, x = map(int, input().split())
a = list(map(int, input().split()))
bool = False
for i in range(n):
    if a[i] == x:
        print("Yes")
        print(i)
        bool = True
        break
if not bool:
    print("No")