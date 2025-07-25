from collections import Counter

n=int(input())

m=list(map(int,input().split()))
c=Counter(m)

for i in c:
    if c[i] != n:
        print(i)

