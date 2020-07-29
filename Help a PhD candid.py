N=int(input())
lst=[]
for i in range(N):
   s=input("")
   if len(s)==3:
     lst.append(s)
for l in lst:
   if l=="P=NP":
     print("skipped")
   else:
     tot=int(l[0])+int(l[2])
     print(tot)
 # The above code gives a runtime error ---> We did not split 2+2 format.
     
N= int(input())
for i in range(N):
  s = input()
  if s == "P=NP":
    print("skipped")
  else:
    l,m = s.split("+")  
    l1 = int(l)
    m1 = int(m)
    print(l1 + m1)
