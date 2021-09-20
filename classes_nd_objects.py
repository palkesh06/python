# Class and object 
class Dog:

	animal = 'dog'	
	
	#  constructor
	def __init__(self, breed):
		
		# Instance Variable
		self.breed = breed			

	# Adds an instance variable
	def setColor(self, color):
		self.color = color
	
	# Retrieves instance variable	
	def getColor(self):	
		return self.color


Rodger = Dog("pug")
Rodger.setColor("brown")
print(Rodger.getColor())
  
#Stack implementation

stack = []
 

stack.append('a')
stack.append('b')
stack.append('c')
 
print('Initial stack')
print(stack)
 

print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
print('\nStack after elements are popped:')
print(stack)


#deque implementation
 
from collections import deque
 
stack = deque()

stack.append('a')
stack.append('b')
stack.append('c')
 
print('Initial stack:')
print(stack)
 

print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
print('\nStack after elements are popped:')
print(stack)

# Queue implementation 
 
from queue import LifoQueue
 

stack = LifoQueue(maxsize = 3)

print(stack.qsize())
  

stack.put('a')
stack.put('b')
stack.put('c')
 
print("Full: ", stack.full())
print("Size: ", stack.qsize())
 

print('\nElements popped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())
 
print("\nEmpty: ", stack.empty())