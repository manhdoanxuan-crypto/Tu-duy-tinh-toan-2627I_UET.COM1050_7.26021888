a = list(map(int, input().split()))
bool = False
a.sort(reverse = True)
for i in range (1,len(a),1):
    if a[i] == a[i-1]: