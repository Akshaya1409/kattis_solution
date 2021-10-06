n=int(input())
lst=[]
j=n-1
for i in range(n):
    a=int(input())
    lst.append(a)
while j>=0:
    print(lst[j])
    j-=1
