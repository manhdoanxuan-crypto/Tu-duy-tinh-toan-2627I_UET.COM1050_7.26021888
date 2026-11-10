n = int(input())
a = list(map(int, input().split()))
b = []
c = []
ch , l = 0, 0
for i in range(n):
    if a[i] > 0:
        # ch+=1
        b.append(a[i])
    else:
        # l+=1
        c.append(a[i])
# print(ch, l)
print(*b)
print(*c)