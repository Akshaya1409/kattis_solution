n=int(input())
lst=[]
for i in range(n):
    x=int(input())
    lst.append(x)

sum_lst=sum(lst)
print(sum_lst-(n-1))
