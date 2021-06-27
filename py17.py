n=int(input("enter n"))
prev=0
pre=1
print(0 ,1,"\t")
for i in range(1,n-1):
    next=prev+pre
    prev=pre
    pre=next
    print(next)
    print("\t")