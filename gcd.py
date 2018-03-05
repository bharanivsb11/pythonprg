a=int(raw_input())
b=int(raw_input())
n=int(raw_input())
for i in range(1,n):
  if(a%i==0 and b%i==0):
    gcd=i 
print gcd    
