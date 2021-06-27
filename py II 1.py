a=int(input("ener a"))
b=int(input("enter b"))
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
print("hcf is",gcd(a,b))
lcm=(a*b)/gcd(a,b)
print("lcm is",lcm)