import sys
import math
def num_sum(n):
    sum=0
    while n>0:
        sum=sum+(n%10)
        n=(int)(math.floor(n/10))
    return sum
    
def p_finder(n):
    digit=num_sum(n)
    p=11
    while True:
        temp_sum=num_sum(n*p)
        if temp_sum==digit:
            return p
        p+=1
lst=[]
for i in sys.stdin:
     if int(i.strip())==0:
         break
     else:
         temp=int(i.strip(" "))
         lst.append(temp)
lst_res=[]
for l in lst:
    res=p_finder(l)
    lst_res.append(res)
for l in lst_res:
    print(l)
