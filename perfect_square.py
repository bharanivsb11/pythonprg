a=int(raw_input())
b=int(raw_input())
c=a*b
p=0
for i in range(2,c):
  if(c==(i*i)):
    p=p+1
if(p==1):
  print "yes"
else:
  print"no"
