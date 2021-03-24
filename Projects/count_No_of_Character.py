def count(st):
 all_freq = {}
 for i in st:
  if i in all_freq:
   all_freq[i] += 1
  else:
   all_freq[i] = 1
 for x in all_freq:
  print(x," = ",all_freq[x])        	

st=input("Enter the string: ")
count(st)
