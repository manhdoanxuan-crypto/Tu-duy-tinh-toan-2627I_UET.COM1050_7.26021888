m , n = map(int, input().split())
if m > n:
   m,n = n,m
for i in range (m,1,-1):
   if n%i == 0 and m%i == 0:
      print(i)
      break
