# cook your dish here

for t in range(int(input())):

    a,b = map(int,input().split())
    c,d = map(int,input().split())
    if((c-a)<0 or (d-b)<0):
        print("IMPOSSIBLE")
    else:
        print("POSSIBLE")