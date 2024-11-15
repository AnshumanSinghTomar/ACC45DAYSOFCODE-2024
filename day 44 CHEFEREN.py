# cook your dish here
t = int(input())

for i in range(t):
    ans = 0 
    n,a,b = map(int,input().split())
    for j in range(1,n+1):
        if j%2 == 0:
            ans+=a
        else:
            ans+=b
    print(ans)