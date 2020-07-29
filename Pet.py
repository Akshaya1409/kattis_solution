n=5
lst=[]
sum=0
for i in range(5):
  a,b,c,d=map(int,input().split())
  sum=a+b+c+d
  lst.append(sum)

maxi=max(lst)
ind=lst.index(max(lst))
print(ind+1," ",maxi)  
