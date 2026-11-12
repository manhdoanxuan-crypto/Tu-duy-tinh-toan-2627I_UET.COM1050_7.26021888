a = list(map(int, input().split()))
bool = False
t = 0
t1 = 0
for i in range (len(a)):
    t2 = 0
    for j in range (2,i**0.5 + 1,1):
        if i%j == 0:
            t2 +=1
    if t2 == 0:
        bool = True
        t += i
        t1 += 1
if bool == False:
    print("-")
else:
    print(f"{(t/t1):.1f}")