n = int(input())
bool = False
for i in range (n):
    i = int(input())
    if i == 42:
        bool = True
        break
if bool == True:
    print("I've found the meaning of life!")
else:
    print("It't a joke!")