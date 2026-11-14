s = input().lower()

d = {}
for ky_tu in s:
    d[ky_tu] = d.get(ky_tu, 0) + 1

ket_qua = [f"{k}:{v}" for k, v in d.items()]
print(" ".join(ket_qua))
