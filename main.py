N=int(input("Введіть ціле число в межах від 1 до 9:" ))
if N<1 or N>9:
  print("Ви ввели чсло яке не входить в межі від 1 до 9")
else:
  for i in range(N,0,-1):
    print("5 " *i)
  for i in range(1,N+1):
    print("5 " *i)
