#!/usr/bin/env python
# coding: utf-8




1. What is the result of the code, and why?
>>> def func(a, b=6, c=8):
print(a, b, c)
>>> func(1, 2)


Ans : 
    
    a and b values are passed from the fucntion but c value is not passed , so default value 8 is taken for the value c.
# In[2]:


def func(a, b=6, c=8):
    print(a, b, c)
func(1, 2)

2. What is the result of this code, and why?
>>> def func(a, b, c=5):
print(a, b, c)
>>> func(1, c=3, b=2)

Ans

The output of the code is 1 2 3.the values passed from the function for a,b and c is 123 respectively.
# In[3]:


def func(a, b, c=5):
    print(a, b, c)
func(1, c=3, b=2)

3. How about this code: what is its result, and why?
>>> def func(a, *pargs):
print(a, pargs)
>>> func(1, 2, 3)

Ans  

The result of the code is 1 (2,3). *pargs stands for variable length  of arguments to be passed by the function. this format is used when we are dont know about the no of arguments to be passed to a function. so all the values under this argument will be stored in a tuple.
# In[4]:


def func(a, *pargs):
    print(a, pargs)
func(1, 2, 3)

4. What does this code print, and why?
>>> def func(a, **kargs):
print(a, kargs)
>>> func(a=1, c=3, b=2)

Ans

The result of the above code is 1 {'c': 3, 'b': 2}. **args stands for variable length keyword arguments. this format is used when we want to  pass the key value pairs as input to a function. All these key value pairs will be stored in a format of dictionary
# In[5]:


def func(a, **kargs):
    print(a, kargs)
func(a=1, c=3, b=2)

5. What gets printed by this, and explain?
>>> def func(a, b, c=8, d=5): print(a, b, c, d)
>>> func(1, *(5, 6))

Ans 

The output is 1 5 6 5,a value is given as 1 and for b and c 5 and 6 is passed through the function as arguments and by defult d value is taken as 5.


# In[7]:


def func(a, b, c=8, d=5): 
    print(a, b, c, d)
func(1, *(5, 6))


# 6. what is the result of this, and explain?
# >>> def func(a, b, c): a = 2; b[0] = 'x'; c['a'] = 'y'
# >>> l=1; m=[1]; n={'a':0}
# >>> func(l, m, n)
# >>> l, m, n
# 
# Ans Ans
# 
# When l,m,n are provided as inputs to the function,its changes the values of l,m,n and sets the value of l=1 ,m=['x'] and n={'a':'y'

# In[11]:


def func(a, b, c): a = 2; b[0] = 'x'; c['a'] = 'y'
l=1; m=[1]; n={'a':0}
func(l, m, n)
l, m, n


