def tim_max(a):
    max_val = max(a)
    vi_tri = [str(i) for i, x in enumerate(a) if x == max_val]
    return f"{max_val} {" ".join(vi_tri)}"

def tim_min(a):
    min_val = min(a)
    vi_tri = [str(i) for i, x in enumerate(a) if x == min_val]
    return f"{min_val} {" ".join(vi_tri)}"

n = int(input())
a = list(map(int, input().split()))
print(tim_max(a))
print(tim_min(a))