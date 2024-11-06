# cook your dish here

i=int(input())
while i>0:

    a,b,c=[int (a) for a in input().split()]
    if ((b*1+c*2)>=a):
        print("Qualify")
    else:
        print("NotQualify")
    i=i-1