def min(a,b):
    if a >= b:
        return b
    else:
        return a
a,b,c = map(int,input().split())
print(min(a,min(b,c)))