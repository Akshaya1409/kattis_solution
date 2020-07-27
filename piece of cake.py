n,h,v=map(int,input().split())
h1=max(h,n-h)
v1=max(v,n-v)
res=h1*v1*4
print(res)
