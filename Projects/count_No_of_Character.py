def count(st):
 freq={}
 for i in st:
  if i in freq:
   freq[i] += 1
  else:
   freq[i] = 1
 for x in freq:
  print(x," = ",freq[x]) 



st=input("Enter the string: ")
count(st)
