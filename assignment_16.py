#!/usr/bin/env python
# coding: utf-8

# 1. Create a list called years_list, starting with the year of your birth, and each year thereafter until the year of your fifth birthday. For example, if you were born in 1980. the list would be years_list = [1980, 1981, 1982, 1983, 1984, 1985].
# 
# 

# Ans

# In[2]:


years_list=[1997, 1998, 1999, 2000, 2001, 2002]


# 2. In which year in years_list was your third birthday? Remember, you were 0 years of age for your first year.
# 
# Ans

# In[3]:


years_list[2]


# 3.In the years list, which year were you the oldest?
# 
# Ans

# In[4]:


years_list[-1]


# 4. Make a list called things with these three strings as elements: "mozzarella", "cinderella", "salmonella".
# 
#     Ans

# In[7]:


things=["mozzarella", "cinderella", "salmonella"]


# 5. Capitalize the element in things that refers to a person and then print the list. Did it change the element in the list?
# 
# Ans

# In[13]:



things = ['mozzarella', 'cinderella','salmonella']

lst = [x.upper() for x in things]
 
print(lst)


# 6. Make a surprise list with the elements "Groucho," "Chico," and "Harpo."
# 
# Ans

# In[33]:


surprise=["Groucho", "Chico","Harpo."]
print(surprise)


# 7. Lowercase the last element of the surprise list, reverse it, and then capitalize it.
# 
# Ans

# In[34]:


print(surprise)
surprise[-1]=surprise[-1].lower()
print(surprise)
surprise[-1]="".join(reversed(surprise[-1]))
print(surprise)


# 8. Make an English-to-French dictionary called e2f and print it. Here are your starter words: dog is chien, cat is chat, and walrus is morse.
# 
# Ans

# In[38]:


efe = {'dog' : 'chien', 'cat' : 'chat',  'walrus' : 'morse'}


# 9. Write the French word for walrus in your three-word dictionary e2f.
# 
# Ans

# In[41]:


print(efe['walrus'])


# 10. Make a French-to-English dictionary called f2e from e2f. Use the items method.
# 
# Ans

# In[46]:


f2e={}
for  key, value in efe.items():
   if value in f2e:
       f2e[value].append(key)
   else:
       f2e[value]=[key]


# 11. Print the English version of the French word chien using f2e.
# 
# Ans

# In[47]:


f2e['chien']


# 12. Make and print a set of English words from the keys in e2f.
# 
# Ans

# In[50]:


for i in efe:
   print(i,":",efe[i])


# 13. Make a multilevel dictionary called life. Use these strings for the topmost keys: 'animals', 'plants', and 'other'. Make the 'animals' key refer to another dictionary with the keys 'cats', 'octopi', and 'emus'. Make the 'cats' key refer to a list of strings with the values 'Henri', 'Grumpy', and 'Lucy'. Make all the other keys refer to empty dictionaries.
# 
#     Ans

# In[68]:







life={'animals':{'cats':['Henri', 'Grumpy', 'Lucy'],'octopi':'', 'emus':''}, 'plants':'','other':''}



# 14. Print the top-level keys of life.
# 
# Ans

# In[64]:


life.keys()


# 15. Print the keys for life['animals'].
# 
# Ans
# 

# In[66]:


life['animals'].keys()


# 16. Print the values for life['animals']['cats']
# 
# Ans

# In[70]:


life['animals']['cats']


# In[ ]:




