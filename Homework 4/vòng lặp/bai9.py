def cpks(x: int) -> bool:
    s = str(x)
    return len(s) == len(set(s))

n = int(input())
a = []

i = 1
while i * i <= n:
    sq = i * i
    if cpks(sq):
        a.append(str(sq))
    i += 1

if a:
    print(" ".join(a))
else:
    print("(no number)")
