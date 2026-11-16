a,b = map(int, input().split())
bool = False
for cho in range(a + 1):
    ga = a - cho
    if ga * 2 + cho * 4 == b:
        print(ga, cho)
        bool = True
        break

if not bool:
    print("invalid")
