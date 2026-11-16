n = int(input())
t = 0
for i in range (n):
    if n%i == 0:
        if i%2 == 0:
            t += 1
print(t)
