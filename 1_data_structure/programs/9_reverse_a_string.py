res=0
negativeNo=0
n = (int(input("enter a number:")))
if (n<0):
  n=-1*n
  negativeNo=-1

while n > 0:
  print(f" loop-----------------------------------------------------{n}")
  rem=n%10
  res=(res*10)+rem
  print( f"new res = {res}")
  n=n//10
  #print( f"new n = {n}")
if (negativeNo < 0):
  res=-1*res

print(res)  








