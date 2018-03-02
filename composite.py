n=int(raw_input())
p=0
for i in range(2,n+1):
  if(n%i==0):
    p=p+1
if(p==1):
  print"no"
else:
  print"yes"
