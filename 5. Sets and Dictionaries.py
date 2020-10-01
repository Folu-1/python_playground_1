#!/usr/bin/env python
# coding: utf-8

# ### Sets and dictionaries
# 
# sets ---> unordered collections with no duplicates
# Set functions use curly brackets {}

# In[1]:


#create a set basket
basket = {'eggs', 'oranges', 'avocado', 'bread'}
print(basket)
type(basket)


# In[3]:


#check for value in basket
is_kiwi = 'kiwi' in basket
print(is_kiwi)


# In[10]:


#list to set conversion
num_list = [1,2,3,4,5,6]
num_set = set(num_list)
print(num_set)
type(num_set)


# In[11]:


num_list1 = [5,6,7,8,9]
num_set1 = set(num_list1)
print(num_set1)
type(num_set1)


# In[29]:


#subtract commom num_set1 values from num_set
num_set - num_set1 


# In[30]:


#list and join both sets without repeating common values
num_set | num_set1 


# In[31]:


#commom values between sets
num_set & num_set1


# In[32]:


#list and join both sets removing common values
num_set ^ num_set1


# In[33]:


#output difference between both sets
print(num_set.difference(num_set1))


# In[34]:


#output both sets without repeating common values
print(num_set.union(num_set1))


# In[35]:


#output the common value between sets
print(num_set.intersection(num_set1))


# ## Dictionaries = Key value pairs

# In[36]:


# Dictionaries - a set of key:value pairs - with the requirement that the 
# keys are unique {within one dictionary}
# use 'dict{}' to create dictionary
# dictionaries are indexed by keys, which can be immutable


# In[38]:


#empty dictionary
empty_dict = {}
print(empty_dict)
type(empty_dict)


# In[39]:


# key value pairs
emp_data = {'Name': 'Antetokumbo', 'Age': 27, 'Height': '6ft 1in', 'Hobby': 'Coding'}
print(emp_data)
type(emp_data)


# In[41]:


#conversion of list to set
list1 = [1,2,3,4]
print(type(list1))
print(list1)
set1 = set(list1)
print(type(set1))
print(set1)


# In[42]:


#convert dict to list
#conversion considers only the keys and not the value
list_emp_data = list(emp_data)
print(type(list_emp_data))
print(list_emp_data)


# In[47]:


#sort data
print(sorted(list_emp_data))


# In[48]:


#extract particular data
emp_height = emp_data['Height']
print(emp_height)


# In[49]:


#updating value of dictionary
emp_data['Age'] = 31
print(emp_data['Age'])


# In[51]:


#add value to dictionary
emp_data['Profession'] = 'Project Management'
emp_data['City'] = 'Toronto'
print(emp_data)


# In[55]:


#get data keys or values in one shot
print(list(emp_data.keys()))
print(list(emp_data.values()))


# In[56]:


#new data sets
new_dict = dict([('Demola',4100), ('Daudu', 4101), ('Folorunsho', 4102)])
new_dict


# In[57]:


#update old data set with new data set
emp_data.update(new_dict)
print(emp_data)


# In[58]:


#delete particular key from a data set
del emp_data['Daudu']
print(emp_data)


# In[67]:


#manipulate data key pairs
student_names = dict([('Tolu', 23), ('Funmi', 35), ('olu', 55), ('Ife', 29)])
print(student_names)

# 2--->key (Katarina, 20) ---> value
student_names[2] = 'Katarina', 20
print(student_names)

# newKey--->key (Katarina, 20) ---> value
student_names['newKey'] = 123
print(student_names)

#print dictionary keys
print(student_names.keys())

#print dictionary pairs
print(student_names.values())


# In[68]:


del student_names[2]
print(student_names)


# In[ ]:


import json

print("STARTING NEW INVOCATION")


def lambda_handler(event, context):
    # TODO implement
    bucket = event[('Records')][0]['bucket']['name']
    region = event[('Records')][0]['awsRegion']
    object = event[('Records')][0]['s3']['object']['key']
    user = event['Records'][0]['userIdentity']['principalId']

    print('bucket ' + bucket)
    print('region ' + region)
    print('user ' + user)

    return (object)
