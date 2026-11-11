import sys

a = []
for line in sys.stdin:
    line = line.strip()
    if line:
        a.append(int(line))
bool = False
a.sort(reverse = True)
t = 0
for i in range(len(a)):
    if i == 0 or a[i] != a[i-1]:
        t += 1
        if t == 3:
            print(a[i])
            found = True
            break
if bool == False:
    print("-")