a=['3','4','7','2','1']
n=len(a)
p=0
for i in range(0,n):
  for j in range(i+1,n):
    if(a[i]>a[j]):
      temp=a[i]
      a[i]=a[j]
      a[j]=temp
for i in range(0,n):      
  p=p+1
if(p>=1):  
  print a     
