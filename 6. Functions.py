#!/usr/bin/env python
# coding: utf-8

# ### Functions

# In[7]:


#a simple function definition
def scream():
    print('***shouts at the top of her voice, HELLO WORLD!')

#call function
scream()


# In[12]:


#return function
def square(num):
    out = num**2
    return(out)
square(3)
sqr_3 = square(3)
print(sqr_3)


# In[14]:


q = square(4)
print("Q is "+str(q))


# In[16]:


#more functions
def factorial(n):
    if n > 1:
        return n*factorial(n-1)
    else:
        return n

fact = factorial(5)
print(fact)


# In[17]:


#functions with arithmetic arguments
def addition(*args):
    print(args)
    return(sum(args))
print(addition(4,5,6,7,8,9))
print(addition(1,2))


# In[23]:


#strip() --> strips string of left and right empty spaces
#split() --> splits string into a list
def randomText(some_text):
    some_text = some_text.strip()
    print(some_text)
    some_text = ' '.join([word[0].upper() + word[1:] for word in some_text.split()])
    print(some_text)
    return(some_text)

outcome = randomText('allen antetokumbo miriam vvvv cccc bbbbb')
print(outcome)


# In[24]:


string_to_list = lambda x: x.split()
print(string_to_list(outcome))
print(type(string_to_list))


# In[ ]:




