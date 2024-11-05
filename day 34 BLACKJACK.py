# cook your dish here
n = int(input())
for i in range(n):
    sum1 = sum(list(map(int, input().split())))
    if (21-sum1) >10 :
        print(-1)
    else:
        print(21-sum1)