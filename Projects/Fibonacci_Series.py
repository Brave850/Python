def fib(n):
  if(n<=2):
    return 1
  else:
    return fib(n-1)+fib(n-2)
  

r=int(input("Enter the limitation for fibonacci series: "))
print("\n")
for i in range(1,r+1):
  print(fib(i),end=' ')
