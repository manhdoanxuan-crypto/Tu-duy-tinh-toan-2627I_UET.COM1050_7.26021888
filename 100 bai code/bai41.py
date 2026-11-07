n = int(input())
a = []
for i in range(n):
    val = map(float, input().split())
    a.append(list(val))
print(list(a))