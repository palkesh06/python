# Taking input from the user
name = input("Enter your name: ")

# Output
print("Hello, " + name)
print(type(name))
num = int(input("Enter a value: "))
 
add = num + 5
 
# Output
print("The sum is %d" %add)   # % is used for formatting like in c 


text = 'this is python'
  
# Splits at space
print(text.split())
  
word = 'geeks, for, geeks'
  
# Splits at ','
print(word.split(','))
  
word = 'geeks:for:geeks'
  
# Splitting at ':'
print(word.split(':'))
  
word = 'CatBatSatFatOr'
  
# Splitting at t
print(word.split('t'))