def hcn(d, r):
    for i in range(r):
        if i == 0 or i == r - 1:
            print("*" * d)
        else:
            if d > 1:
                print("*" + " " * (d - 2) + "*")
            else:
                print("*")

d, r = map(int, input().split())
hcn(d, r)
