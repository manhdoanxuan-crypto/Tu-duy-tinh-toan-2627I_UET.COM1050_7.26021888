a, b = map(float, input().split())
if a == b == 0:
    print("Vo so nghiem")
elif a == 0 and b!= 0:
    print("Vo nghiem")
else:
    print(-b/a)