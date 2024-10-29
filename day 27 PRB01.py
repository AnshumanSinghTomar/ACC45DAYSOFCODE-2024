# cook your dish here
prime=int(input())
for p in range(prime):
  r=int(input())
  e=0
  for i in range(1,r+1):
    if r%i==0:e+=1
  print("yes") if e==2 else print("no")