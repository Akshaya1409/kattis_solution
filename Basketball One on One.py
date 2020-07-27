a=input("")
c=0
d=0
for char in a:
  if char=="A":
     c+=1         # For counting no.of occurances of char A
  elif char=="B":
     d+=1         # similarly for B
if c>d:
  print("A")
else:
  print("B")
