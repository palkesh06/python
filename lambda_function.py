# use of lambda 
raise_to_power = lambda x, y: x ** y

raise_to_power(2, 3)

# use of map 
nums = [48, 6, 9, 21, 1]

square_all = map(lambda num: num ** 2, nums)

print(list(square_all))

# use of filters 
my_list = [12, 65, 54, 39, 102, 339, 221, 50, 70, ]
  
result = list(filter(lambda x: (x % 13 == 0), my_list)) 
  
print(result) 
# use fo reduce 
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print (sum)