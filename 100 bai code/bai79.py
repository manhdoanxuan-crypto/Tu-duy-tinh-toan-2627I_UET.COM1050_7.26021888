s = input().lower()
d = {}
for ky_tu in s:
    if ky_tu != ' ':
        d[ky_tu] = d.get(ky_tu, 0) + 1
a = ''
max = 0
for ky_tu in s:
    if ky_tu != ' ' and d[ky_tu] > max:
        max = d[ky_tu]
        a = ky_tu
if max > 0:
    print(f"{a}:{max}")
