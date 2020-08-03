x,y,n=map(int,input().split())
i=1
while i<=n:
   if i%x==0:
     if i%y==0:
       print("FizzBuzz")
     else:
        print("Fizz")
   elif i%y==0:
     print("Buzz")
  
   else:
     print(i)
   i+=1
