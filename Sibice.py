import sys
import math
count=0
h=0
w=0
lst=[]
for i in sys.stdin:
    if i.strip()=="":
       break
    elif count==0:
        t=i.split(" ")
        w=int(t[1])
        h=int(t[2])
        count+=1
    else:
         lst.append(int(i.strip()))
d=int(math.sqrt(math.pow(w,2)+math.pow(h,2)))
for m in lst:
    if m<=d:
        print("DA")
    else:
        print("NE")
