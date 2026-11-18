def max(a):
    max_val = max(a)
    vi_tri = [str(i) for i, x in enumerate(a) if x == max_val]
    print(max_val, " ".join(vi_tri))

def min(a):
    min_val = min(a)
    vi_tri = [str(i) for i, x in enumerate(a) if x == min_val]
    print(min_val, " ".join(vi_tri))

n = int(input())
a = list(map(int, input().split()))
print(max(a), min(a))
