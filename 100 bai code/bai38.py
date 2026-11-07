k = int(input())
t = 0
for i in range (2, 10**18):
    t1 = 0
    for j in range (1 , round(i**0.5)+1):
        if i % j == 0:
            t1+=1
    if t1 == 1:
        print(i , end = " ")
        t+=1
    if t == k:
        break