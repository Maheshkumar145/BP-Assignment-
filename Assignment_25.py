#!/usr/bin/env python
# coding: utf-8

# 1) What is the difference between enclosing a list comprehension in square brackets and parentheses?
# 
# Ans
# 
# If we enclose  the list comprehension in square brackets then it will returns a list after execution of the code but where as if we enclose the list comprehension in parentheses returns a generator object.
# 

#  2) What is the relationship between generators and iterators?
# 
# Ans
# 
# Generator Expressions are  similar to list comprehensions, but the  doesn’t construct list object, Instead of creating a list and storing the whole sequence of data in the memory, the generator generates the next element in the code.
# When  there  is a normal function which having the  return statement is called, it terminates whenever it gets a return statement, But a function with a yield statement like it is used in the generator it actually saves the state of the function and can be started it again from the same state from the next time the function is called.
# The Generator Expression allows us to create a generator without the yield keyword.
# Parenthesis are used in place of square brackets.
# 
# Iterators method used in python is a object used to iterate over the objects like tuples,dicts and sets.The iterator object is initialized using the iter() method then with that there should be the next() method for iteration.
# __iter__()-The iter() method is  used  and called for the initialization of an iterator. This returns an iterator object and__next__()-The next method returns the next value for the iterable, If we use a for loop for the any iterable object, it  internally  uses the iter() method to get an iterator object, which further uses the next() method to iterate over. 
# 
# 
#     

# 3) What are the signs that a function is a generator function?
# 
# Ans
# 
# A generator function will always uses a yield statement instead of a return statementwhich generally used for other functions but A generator function will always return a iterable object called generator, where as a normal function can return a string/list/tuple/dict/NoneType.
# 
# 

# 4) What is the purpose of a yield statement?
# 
# Ans
# 
# The yield statement in the code stops and returns the value to the caller but it has the state of the information it holds and can be resumes back when is is necessary so that it can execute and continues the code.It prodce a series of values over the time.

# 5) What is the relationship between map calls and list comprehensions? Make a comparison and contrast between the two.
# 
# Ans
# 
# 1.List comprehension has a  very simpler configuration when compared with the map function.  
# 2.List comprehension can be used together with if condition as replacement of filter method,but in the Map function there is  no such functionality, but we can ge the map function output for which the input is given by the filter function.  
# 3.List comprehension  will returns a list, whereas the map function returns an object of Iterable type when code is executed.  
# 4.List comprehension execution is faster than that of map function when the formula expression used in the code is  complex. 
# 5.Map function is faster than list comprehension when the formula is already defined as a function earlier. So, that map function is used without lambda expression. 
# 
# 
