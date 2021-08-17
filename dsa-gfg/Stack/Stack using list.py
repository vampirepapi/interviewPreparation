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