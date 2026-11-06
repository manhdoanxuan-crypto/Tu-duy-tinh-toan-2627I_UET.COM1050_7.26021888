n = int(input())
if n < 3:
    print("-")
else:
    for i in range (1, n+1):
        if i% 3 == 0:
            print(i, end=" ")