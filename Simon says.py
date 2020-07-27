n=int(input())
sub="Simon says"
len=len(sub)
for i in range(n):
  s=input()
  if (s.find(sub)!=-1): #find() --> returns -1 if the substring is not found
    print(s[len:])
