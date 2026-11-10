a = list(map(int, input().split()))
t = 0
b = -10*18
bool = False
for i in range(a):
    if a[i] > b and a[i] < 0:
        b = a[i]
        bool = True
if bool == False:
    print("-")
else:
    print(b)