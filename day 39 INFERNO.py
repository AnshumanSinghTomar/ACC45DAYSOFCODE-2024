# cook your dish here
from math import ceil
t = int(input())
for _ in range(t):
    Enemies, Single_damage = map(int, input().split())
    Health = list(map(int, input().split()))
    Multi_Hits = max(Health)
    Single_Hits = 0
    for Bar in Health:
        Single_Hits += ceil(Bar / Single_damage)
    print(min(Single_Hits, Multi_Hits))