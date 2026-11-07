n = int(input())
a = []
for i in range(n):
    val = map(float, input().split())
    a.append(list(val))
t=sum(list(a))
print(t)