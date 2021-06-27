n=int(input("enter n"))
l=int(input("enter l"))
for k in range(n,l):
   if k>1:   
      for i in range(2,k-1):
            if (k%i)==0:
                break
      else:
       print("k=",k)
                
              
