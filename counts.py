# Keith Brazill
# G00387845

# Write a Python function called counts that takes a list as
# input and returns a dictionary of unique items in the list as keys and the number of
# times each item appears as values. So, the input ['A', 'A', 'B', 'C', 'A']
# should have output {'A': 3, 'B': 1, 'C': 1} . Your code should not depend
# on any module from the standard library or otherwise. You should research the task
# first and include a description with references of your algorithm in the notebook.

# First we are going to create a list
lst = [] 
  
# We then prompt the user to tell us how many elements are in this list
n = int(input("Enter number of items in list: ")) 
  
# We then tell python to let the user input the items in the list from 0 to total number input (n)
for i in range(0, n): 
    item = (input()) 
  
    lst.append(item) # adding the items to the list

dict((x, lst.count(x)) for x in lst) # Here we tell python using the dict comamand that for each item in the list (x)
                                     # we want a count of the number of times the item (x) appears in the list
