import sys

a = []
for line in sys.stdin:
    a.append(int(line))
bool = False
a.sort(reverse = True)
for i in range (2,len(a),1):
    if a[i] != a[i-1]:
        if a[i-1] != a[i-2]:
            print(a[i])
            bool = True
            break
if bool == False:
    print("-")