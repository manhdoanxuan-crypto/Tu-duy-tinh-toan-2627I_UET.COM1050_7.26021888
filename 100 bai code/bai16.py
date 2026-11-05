a , b = map(float, input().split())
c = (a + b*2)/3
print(f"{c:.1f}")
print("Gioi" if c >= 8 else "Kha" if 8 > c >= 6.5 else "Trung binh" if 6.5 > c >= 5.0 else "Yeu" if 5.0 > c >= 3.5 else "Kem")