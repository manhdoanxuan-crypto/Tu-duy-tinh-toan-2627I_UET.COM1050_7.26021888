n = int(input())
k = 0
S = 0
while S + k + 1 < n:
    k += 1
    S += k
print(k)
