x = int(input())
if x == -1:
    print("Dãy không có số nào hợp lệ.")
else:
    max = x
    min = x
    while True:
        x = int(input())
        if x == -1:
            break
        if x > max:
            max = x
        if x < min:
            min = x

    print(max)
    print(min)
