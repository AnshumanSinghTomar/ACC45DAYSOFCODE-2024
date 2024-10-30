# cook your dish her
t=int(input())
for i in range(t):
    x,y,k=map(int,input().split())
    if x>y:
        s=(x-y)//k
        if (x-y)%k>0:
            s+=1
    else:
        s=(y-x)//k
        if(x-y)%k>0:
            s+=1
    print(s)        
