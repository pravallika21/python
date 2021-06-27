num=int(input("num"))
count=0
for i in range(2,num-1):
  if num%i==0:
     count=count+1
if count==0:
    print("prime")
else:
      print(" not prime number")
