a=int(input("enter a"))
b=int(input("enter b"))
def hcf(a,b):
         if b==0:
                    return a
         else:
                    return hcf(b,a%b)
print("hcf is",hcf(a,b))            