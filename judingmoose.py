l,r=map(int,input().split())
k=0
tot=0
if l==r and l!=0 and r!=0 :
   print("Even",l+r)
elif l!=r:
  k=max(l,r)
  #tot=2k
  print("Odd",2*k)
elif l==0 and r==0:
   print("Not a moose")
