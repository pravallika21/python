def fib(n):
    if n<=1:
        return n;
    else:
        return (fib(n-1)+fib(n-2))
n=int(input("no. of terms"))
if n<=0:
    print("please enter positve no.")
else:
    for i in range(0,n):
        print(fib(i))
  