n=int(input("enter number"))
num=n
k=0
while n!=0:  
      d=n%10
      k=k+(d**3)
      n=n//10
if(k==num):
    print(":)")
else:
    print(":(")