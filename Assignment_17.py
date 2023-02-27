#!/usr/bin/env python
# coding: utf-8

# 1. Assign the value 7 to the variable guess_me. Then, write the conditional tests (if, else, and elif) to
# print the string &#39;too low&#39; if guess_me is less than 7, &#39;too high&#39; if greater than 7, and &#39;just right&#39; if equal
# to 7.
# 
# Ans

# In[9]:


guess_me=7

if   guess_me <7 :
     print('too low')
        
elif  guess_me>7 :
      print('too high')
        
else : 
    print('just right')    


# 2. Assign the value 7 to the variable guess_me and the value 1 to the variable start. Write a while
# loop that compares start with guess_me. Print too low if start is less than guess me. If start equals
# guess_me, print &#39;found it!&#39; and exit the loop. If start is greater than guess_me, print &#39;oops&#39; and exit
# the loop. Increment start at the end of the loop.
# 
# Ans

# In[63]:


guess_me=7
start=1


while True:
    if start < guess_me:
        print('too low')
    elif start == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break
    start += 1


# 3. Print the following values of the list [3, 2, 1, 0] using a for loop.
# 
# Ans 
# 

# In[67]:


list=[3,2,1,0]
for i in list:
    print(i);


# 4. Use a list comprehension to make a list of the even numbers in range(10)
# 
# Ans

# In[85]:


list=[i for i in range(10) if i%2==0]
     
print(list)


# 5. Use a dictionary comprehension to create the dictionary squares. Use range(10) to return the
# keys, and use the square of each key as its value.
# 
# Ans

# In[78]:


squares ={k:k*k for k in range(10)  }

squares


# 6. Construct the set odd from the odd numbers in the range using a set comprehension (10).
# 
# Ans

# In[89]:


odd=[i for i in range(10) if i%2!=0]
print(odd)


# 7. Use a generator comprehension to return the string &#39;Got &#39; and a number for the numbers in
# range(10). Iterate through this by using a for loop.
# 
# Ans

# In[95]:



string = ('Got ' + str(n) for n in range(10))
for item in string :
    print(item)


# 8. Define a function called good that returns the list [&#39;Harry&#39;, &#39;Ron&#39;, &#39;Hermione&#39;].
# 
#  Ans

# In[97]:


def good():
    return ['Harry','Ron','Hermione']


# 9. Define a generator function called get_odds that returns the odd numbers from range(10). Use a
# for loop to find and print the third value returned.
# Ans

# In[115]:



get_odds = (num for num in range(10) if not num % 2 == 0)
count = 0
for num in get_odds:
    if count == 2:
        print(num)
        break
    count += 1


# 10. Define an exception called OopsException. Raise this exception to see what happens. Then write
# the code to catch this exception and print &#39;Caught an oops&#39;.
# 
# Ans

# In[116]:


class OopsException(Exception):
    pass


def with_exception(a):
    if a < 0:
        raise OopsException(a)


try:
    with_exception(-1)
except OopsException as err:
    print('Caught an oops')


# 11. Use zip() to make a dictionary called movies that pairs these lists: titles = [&#39;Creature of Habit&#39;,
# &#39;Crewel Fate&#39;] and plots = [&#39;A nun turns into a monster&#39;, &#39;A haunted yarn shop&#39;].
#  
#                                                                                    
# Ans                                                                                 

# In[117]:


titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']

movies = {}
for title, plot in zip(titles, plots):
    movies[title] = plot
print(movies)

