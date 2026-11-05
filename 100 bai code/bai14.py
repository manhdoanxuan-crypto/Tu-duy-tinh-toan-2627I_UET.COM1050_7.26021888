t = int(input())
print(
"Thieu nhi" if 0 < t <= 11 else
"Thieu nien" if 11 < t <= 25 else
"Trung nien" if 25 < t <= 50 else
"Lao nien")