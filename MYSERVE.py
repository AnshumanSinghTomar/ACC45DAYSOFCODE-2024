# cook your dish here

for i in range(int(input())):

    p,q=map(int,input().split())
    a=p+q
    if a%4==0 or a%4==1:
        print("alice")
    else:
        print("bob")