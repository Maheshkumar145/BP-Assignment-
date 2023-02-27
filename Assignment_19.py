#!/usr/bin/env python
# coding: utf-8

# 1. Make a class called Thing with no contents and print it. Then, create an object called example from this class and also print it. Are the printed values the same or different?
# 
# 
# Ans:
#    

# In[9]:


class thing:
   print()
example=thing()


# both have same values 

# 2. Create a new class called Thing2 and add the value 'abc' to the letters class attribute. Letters should be printed.
# 
# Ans

# In[7]:


class thing2 :
    attribute='abc'
p=thing2()
print(p.attribute)


# 3. Make yet another class called, of course, Thing3. This time, assign the value 'xyz' to an instance (object) attribute called letters. Print letters. Do you need to make an object from the class to do this?
# 
# ANs

# In[23]:


class thing3:
    def __init__(self):
        self.letters='xyz'
a= thing3()
print(a.letters)       


# 4. Create an Element class with the instance attributes name, symbol, and number. Create a class object with the values 'Hydrogen,' 'H,' and 1.
# 
# ANs

# In[27]:


class Element:
    def __init__(self,name,symbol,number):
          self.name=name
          self.symbol=symbol
          self.number=number
hyd=Element('Hydrogen','H','1')


# 5. Make a dictionary with these keys and values: 'name': 'Hydrogen', 'symbol': 'H', 'number': 1. Then, create an object called hydrogen from class Element using this dictionary.
# 
# ANS

# In[34]:


dict={'name':'Hydrogen','symbol':'H','number': 1}

hydrogen = Element(dict['name'], dict['symbol'], dict['number'])

hydrogen.name


# 6. For the Element class, define a method called dump() that prints the values of the object’s attributes (name, symbol, and number). Create the hydrogen object from this new definition and use dump() to print its attributes.
# 
# ANS

# In[41]:


class Element:
       def __init__(self,name,symbol,number):
           self.name=name
           self.symbol=symbol
           self.number=number
       def dump(self):
            print('name=%s, symbol=%s, number=%s' %(self.name, self.symbol, self.number))
  
hydrogen=Element('Hydrogen','H','1')
hydrogen.dump()


# 7. Call print(hydrogen). In the definition of Element, change the name of method dump to __str__, create a new hydrogen object, and call print(hydrogen) again.
# 
# ANS

# In[43]:


class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        return ('name=%s, symbol=%s, number=%s' %(self.name, self.symbol, self.number))

hydrogen = Element('Hydrogen','H','1')
print(hydrogen)


# 8. Modify Element to make the attributes name, symbol, and number private. Define a getter property for each to return its value.
# 
# ANS

# In[44]:


class Element:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
       
    def name(self):
        return self.__name

    def symbol(self):
        return self.__symbol
  
    def number(self):
        return self.__number
hydrogen = Element('Hydrogen', 'H', 1)


# 9. Define three classes: Bear, Rabbit, and Octothorpe. For each, define only one method: eats(). This should return 'berries' (Bear), 'clover' (Rabbit), or 'campers' (Octothorpe). Create one object from each and print what it eats.
# 
#  ANS

# In[45]:


class Bear:
    def eats(self):
        return 'berries'
    
class Rabbit:
    def eats(self):
        return 'clover'

class Octothorpe:
    def eats(self):
        return 'campers'
    
b = Bear()
r = Rabbit()
o = Octothorpe()


# 10. Define these classes: Laser, Claw, and SmartPhone. Each has only one method: does(). This returns 'disintegrate' (Laser), 'crush' (Claw), or 'ring' (SmartPhone). Then, define the class Robot that has one instance (object) of each of these. Define a does() method for the Robot that prints what its component objects do.
# 
# ANS
# 

# In[50]:


class Laser:
    def does(self):
        return 'disintegrate'

class Claw:
    def does(self):
        return 'crush'
    
class SmartPhone:
    def does(self):
        return 'ring'
    
class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()
        
    def does(self):
        return '''I have many attachments:
        My laser, to %s.
        My claw, to %s.
        My smartphone, to %s.''' % (self.laser.does(),self.claw.does(),self.smartphone.does() )
r=Robot()
print(r.does())


# In[ ]:





# In[ ]:





# In[ ]:




