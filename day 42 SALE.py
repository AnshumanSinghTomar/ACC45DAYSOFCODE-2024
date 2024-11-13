# cook your dish here
for i in range(int(input())):
    x=list(map(int,input().split()))
    print(sum(x)-min(x))