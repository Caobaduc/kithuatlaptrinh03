for i in range(2,101):
      dem=0
      for j in range(2,101):
           if i%j==0:
               dem=dem+1
      if dem ==1:
           print(i)
