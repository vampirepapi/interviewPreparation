#using list to implement stack

#resource link:-https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/5_Stack/5_stack.ipynb

s=[]
s.append("google.com")
s.append("google.com/china")
s.append("google.com/india")
s.append("google.com/usa")


#popping elements
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())

#now our list is empty if we again try to pop(), it'll show 'pop from empty list' error
print(s.pop())

print(s)

#in python if we just want to access last element we can use list index [-1]
print(s[-1])

#note:- the problem is with py list is that it is dynamic so its memory costly



#Stack implementation using collections.deque

from collections import deque
stack =  deque() #creating instance of deque

#print(dir(stack)) #this will show every function availabe for deque

stack.append("google.com")
stack.append("google.com/china")
stack.append("google.com/india")
stack.append("google.com/usa")

print(stack.pop())
print(stack[-1])




#Creating Stack function class using collections.deque for [ proper stack implementation ]
from collections import deque
class Stack:
	def __init__(self):
		self.conatiner = deque() #object of deque class

	def push(self, val):
		self.conatiner.append(val)

	def pop(self):
		return self.conatiner.pop()

	def peek(self):
		return self.conatiner[-1]

	def is_empty(self):
		return len(self.conatiner) == 0

	def size(self):
		return len(self.conatiner)


s=Stack() #object of stack class
s.push(5)
s.push(6)
s.push(7)
s.push(8)

print(s)
#pop func
print(s.pop())
#is_empty func
print(s.is_empty())
#returns size
print(s.size())
#peeking last element
print(s.peek())

s.pop()
s.pop()
s.pop() #popped all elem
s.pop() #mow it will show error