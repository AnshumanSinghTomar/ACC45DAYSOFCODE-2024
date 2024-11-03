sai=int(input())
p1=0
p2=0
m1=0
m2=0
for i in range(sai):
    a,b=map(int,input().split())
    m1 += a
    m2 += b
    if m1>m2:
        p1 = max(p1,m1-m2)
    else:
        p2 = max(p2,m2-m1)
if p1>p2:
    print(1,p1)
else:
    print(2,p2)
