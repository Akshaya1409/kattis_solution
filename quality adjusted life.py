n=int(input())
i=1
sum=0.0
while i<=n:
    q,y=map(float,input().split())
    sum+=q*y
    i+=1
print(round(sum,5))
