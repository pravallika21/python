num=int(input("enter number"))
l=int(input("enter upper"))
for n in range(num,l+1):
  m=n
  k=0
  while n!=0:  
      d=n%10
      k=k+(d**3)
      n=n//10
  if k==m:
       print(k)

