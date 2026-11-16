def reverse_num(n):
    return int(str(n)[::-1])

n = int(input())
t = 0

while n != reverse_num(n):
    n = n + reverse_num(n)
    t += 1

print(t,n)
