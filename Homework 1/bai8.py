s = input()
a = input()
b = input()
s = s[12:]
a = int(a[20:])
d = int(b[18:])
c = d - a
print("Ho va ten:" , s)
if 0 < c < 50:
    print("Tien phai tra la:", round(1984*c*1.08))
elif 50 <= c < 100:
    print("Tien phai tra la:", (round((1984*50 + 2050*(c - 50))*1.08)))
elif 101 <= c < 200:
    print("Tien phai tra la:", (round((1984*50 + 2050*50 + 2380*(c - 100))*1.08)))
elif 201 <= c < 300:
    print("Tien phai tra la:", (round((1984*50 + 2050*50 + 2380*100 + 2998*(c - 200))*1.08)))
elif 301 <= c < 400:
    print("Tien phai tra la:", (round((1984*50 + 2050*50 + 2380*100 + 2998*100 + 3350*(c - 300))*1.08)))
else:
    print("Tien phai tra la:", (round((1984*50 + 2050*50 + 2380*100 + 2998*100 + 3350*100 + 3460*(c - 400))*1.08)))

