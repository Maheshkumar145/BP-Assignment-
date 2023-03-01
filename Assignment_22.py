#!/usr/bin/env python
# coding: utf-8
1. What is the result of the code, and explain?


>>> X = 'iNeuron'
>>> def func():
print(X)


>>> func()


Ans:

The output of the function is ineuron.



# In[1]:


X = 'iNeuron'
def func():
    print(X)
func()

2. What is the result of the code, and explain?


>>> X = 'iNeuron'
>>> def func():
X = 'NI!'


>>> func()
>>> print(X)

Ans

The output of the function is ineuron because x value is not getting printed inside the loop, so global value of x will be printed.

# In[5]:


X = 'iNeuron'
def func():
     X = 'NI!'
func()
print(X)

3. What does this code print, and why?


>>> X = 'iNeuron'
>>> def func():
X = 'NI'
print(X)


>>> func()
>>> print(X)

Ans

The output will be Ni and iNeuron,First the local value of X is printed and then global value of X will be printed

# In[6]:


X = 'iNeuron'
def func():
    X = 'NI'
    print(X)


func()
print(X)

4. What output does this code produce? Why?


>>> X = 'iNeuron'
>>> def func():
global X
X = 'NI'


>>> func()
>>> print(X)

Ans

Here global X value is defined inside the def function() so, the value of X NI will be same everwhere in the code.


# In[7]:


X = 'iNeuron'
def func():
    global X
    X = 'NI'


func()
print(X)

5. What about this code—what’s the output, and why?


>>> X = 'iNeuron'
>>> def func():
X = 'NI'
def nested():
print(X)
nested()


>>> func()
>>> X


Ans  

The output of the code is NI and iNeuron. the reason for this output is if a function wants to access a variable, if its not available in its localscope. it looks for the variable in its global scope. similarly here also function nested looks for variable X in its global scope. hence the output of the code is NI
# In[18]:


X = 'iNeuron'
def func():
    X = 'NI'
    def nested():
        print(X)
    nested()


func()

X

6. How about this code: what is its output in Python 3, and explain?


>>> def func():
X = 'NI'
def nested():
nonlocal X
X = 'Spam'
nested()
print(X)


>>> func()

Ans

The output of the code is Spam. nonlocal keyword in python is generally used to declare a variable as not local.Hence the X = "Spam" is defined as  the global scope value. hence the output of print(X) statement is Spam


# In[24]:


def func():
    X = 'NI'
    def nested():
        nonlocal X
        X = 'Spam'
    nested()
    print(X)


func()

