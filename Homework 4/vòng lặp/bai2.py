while True:
    n = int(input())
    if n > 0:
        break
bool == True
for i in range (2,int(n**0.5 + 1),1):
    if n%i == 0:
        bool = False
        break
if bool == True:
    print("Yes")
else:
    print("No")