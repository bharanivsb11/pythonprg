a=int(raw_input())
n=len(a)
for i in range(0,n):
  for j in range(i+1,n):
    if(a[i]>a[j]):
      temp=a[i]
      a[i]=a[i+1]
      a[i+1]=temp
print a[i]      
