n = int(input())
bool = False
for i in range(n,1,-1):
    if n % i == 0:
        t = 0
        for j in range (2,int(i**0.5+1),1):
            if i%j ==0:
                t+=1
            if t == 0:
                bool = True
    if bool == True:
        print(i)
        break