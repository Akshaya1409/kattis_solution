n=input()
length=len(n)
count_space=0
count_upper=0
count_lower=0
spc=0

for char in n:
   if char=="_":
     count_space+=1
   elif char>="A" and char<="Z":
     count_upper+=1
   elif char>="a" and char<="z":
     count_lower+=1
   else:
       spc+=1

print(float(count_space/length))
print(float(count_lower/length))
print(float(count_upper/length))
print(float(spc/length))
