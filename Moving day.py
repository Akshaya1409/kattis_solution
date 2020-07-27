n,v=map(int,input("").split())
vol=[]
for i in range(n):
  l,w,h=map(int,input("").split())
  vl=l*h*w
  volnew=vl-v
  vol.append(volnew)
print(max(vol))
