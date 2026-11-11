import sys
g=0
a = [4,5,7]
while True:
    i=int(input())
    a.append(i)
    g+=1
    if g==10: break
print(a)
    
# bool = False
# a.sort(reverse = True)
# t = 0
# for i in range(len(a)):
#     if i == 0 or a[i] != a[i-1]:
#         t += 1
#         if t == 3:
#             print(a[i])
#             found = True
#             break
# if bool == False:
#     print("-")