#!/usr/bin/env python
# coding: utf-8

# 1. What is the relationship between def statements and lambda expressions ?
# 
# Ans: 
# 
#    Both lambda and def  will create the same kind of function and have the same kind of data and capabilities,but Their is a    
#    difference in the syntac.
#    A lambda is an expression producing a function but  def is a statement producing a function.
#     
#     

# 2. What is the benefit of lambda?
# 
# Ans:
# 
#     1.No need of using the return statement because by default lambda will return the valuees
#     2.Execution time for program is fast for the same operation comapred using def.
#     3.We can define a function in a single line of code and use it immediately.  

# 3. Compare and contrast map, filter, and reduce.
# 
# Ans:
# 
# 
#     Map, Filter, and Reduce are used in the functional programming which allows the programmer  to write simpler, shorter code, without neccessarily needing to bother about loops and branching.
#     map and filter come built-in with Python (in the __builtins__ module) and require no importing but reduce needs to be imported as it resides in the functools module.
#     The map() function in python has the syntax map(func, *iterables)
#     Where func is the function on which each element in iterables.
#     
#     filter() requires the function to return boolean values (true or false) and then passes each element in the iterable through the function,  which filters away those that are false
#     It has the following syntax:filter(func, iterable),Unlike map(), only one iterable is required.
#     
#     reduce() will be applied to the  function of two arguments one to the elements of an iterable, and another optionally starting with an initial argument. 
#     It has the following syntax:reduce(func, iterable[, initial]).
#     func requires two arguments, the first of which is the first element in iterable (if initial is not supplied) and the second element in iterable.
#     If initial is supplied, then it becomes the first argument to func and the first element in iterable becomes the second element.

# 4. What are function annotations, and how are they used?
# 
# Ans:
#     
#     Function annotations are some random expressions which are written with the functions used and they will be evaluated at         compile time but They will  not be exist at the run time of the code, and there is no meaning of these expressions to   
#     python.They are used and interpreted by a third party or external python libraries.
# 
#     Annotations of simple parameters def func(x: expression, y: expression = 20):
#     Whereas the annotations for excess parameters are as − def func (**args: expression, **kwargs: expression):

# 5. What are recursive functions, and how are they used?
# 
# 
# Ans
# 
#    Recursion is a  programming concept, It means that a function calls itself and This has the benefit of calling a  loop    
#    through function recursive until it reach a result.
#    The code below shows us how a recursive function works by calling a recursive function factorial again and again until x is   
#    equal to 1.
# 
# 

# In[2]:


def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
num = 3
print("The factorial of ", num, "is", factorial(num))


# 6. What are some general design guidelines for coding functions?
# 
# Ans:
#     
#     1.Using a docstring and explaining the function inside it helps to understand the code very well.
#     2.Use a tab for indentation.
#     3.Follow the same case for variables, constants, classes and functions across the program.
#     4.Avoid using or limited use of global variables.
#     5.Always try to use a name for the function which conveys the purpose of the function.

# 7. Name three or more ways that functions can communicate results to a caller.
# 
# Ans:
#     
#     print,return and yield
#     

# In[ ]:




