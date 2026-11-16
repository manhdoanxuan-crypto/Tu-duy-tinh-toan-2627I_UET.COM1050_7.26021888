n = int(input())
bool = False
a = list(map(int,input().split()))
for i in range (n):
    if a[i] == 42:
        bool = True
        break
if bool == True:
    print("I've found the meaning of life!")
else:
    print("It's a joke!")