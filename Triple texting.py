# THE ABOVE GIVEN CODE CORESPONDS TO THE EXPECTED OUTPUT,BUT YIELDS RUN TIME ERROR


s=input("")
l=len(s)
count=0
if l>=3 and l<=99:
 for char in s[1:-1]:
     count+=1
     if s[0]==char:
       t=s[0:count]
       break
  print(t)
