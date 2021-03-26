def fib(n):
  if(n<=2):
    return 1
  else:
    return fib(n-1)+fib(n-2)
  

while true:
  try:
    r=input("Enter the position of the fibonacci sequence")
    r=int(r)
    break
   except ValueError:
    print("Invalid Input please enter an integer value!!")

print("\n")
for i in range(1,r+1):
  print(fib(i),end=' ')
