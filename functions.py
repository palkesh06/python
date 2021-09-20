def myfun( ):
    print( "This is my function ")

myfun() 
def myfunction( *var):
    for i in var:
     print(i)

myfunction(1,2,3,4)

# Recusion 
def rec(k):
  if(k > 0):
    result = k + rec(k - 1)
  else:
    result = 0
  return result
print ( "Result of rec is :", rec(5))
