#!/usr/bin/env python
# coding: utf-8

# ### Python collections (Arrays)
# 
# List ---> ordered and duplicable members<br>
# Tuple ---> ordered, unchangeable, duplicable<br>
# Set ---> unordered and unindexed. No duplicate<br>
# Dictionary ---> unordered, changeable and indexed. No duplicate

# In[12]:


#How to create a list
createList = []
print(createList)
type(createList)


# In[13]:


#create a list with a constructor
listConst = list()
type(listConst)


# ### List methods
# 
# appen() --> add to end of list<br>
# insert() --> add to specific location<br>
# extend() --> add to list or any iterable --> end of current list<br>
# copy() --> return copy of list<br>
# count() --> # of elements in list<br>
# clear() --> remove element from list<br>
# index() --> index of first element with specific value<br>
# remove() --> remove item with specific value<br>
# pop() --> remove element at specific position<br>
# reverse() --> reverse order of list<br>
# sort() --> sorts the list<br>
# join() ---> adds after each character

# In[37]:


#Data structures
fruits = ['Banana', 'Oranges', 'Avocado', 'Lemons', 'Oranges',
          'Strawberries', 'Tangerines','blue berries','Oranges','pear',
         'Lemons', 'apple','kiwi','Oranges']
numbers = ['1','2','34','56','100','34','2','34','5','76','34']

#count element in a list
num_of_oranges = fruits.count('Oranges')
print(num_of_oranges)
print(numbers.count('34'))

#find an index
indexOranges = fruits.index('Oranges')
print(indexOranges)

indexKiwi = fruits.index('kiwi')
print(indexKiwi)

#reverse order
fruits.reverse()
print(fruits)


# In[19]:


#append to the list
numbers.append('456')
print(numbers)

#sort list
fruits.sort()
numbers.sort()
print(fruits)
print(numbers)


# In[31]:


#pop removes element at location
fruits.pop()
print(fruits[0])
print(fruits)
print(fruits[2:11])  #starts at 2 end ends at 10

#append 
print(fruits.append('blue berries'))


# In[43]:


#fruits = ['Banana', 'Oranges', 'Avocado', 'Lemons', 'Oranges',
#         'Strawberries', 'Tangerines,','blue berries','Oranges','pear',
#        'Lemons', 'apple','kiwi','Oranges']
fruits


# In[40]:


#print tangerine in +ve and -ve directions
print(fruits[7])
print(fruits[-7])
print(fruits[:-3])


# In[51]:


#remove elements
no_Oranges = fruits.append('Oranges')
print(fruits)


# In[53]:


newFruitsList = fruits  #same as newFruitsList = fruits.copy()
print(newFruitsList)
newFruitsList.sort()
print(newFruitsList)
newFruitsList.append('guava, lime, pear')
print(newFruitsList)


# In[55]:


print(id(newFruitsList))
another_list = newFruitsList.copy()
print(id(another_list))


# In[58]:


#split words in a sentence
a_sentence = 'Corona virus is ravaging the world right now.'
words_in_sentence = a_sentence.split()
print(words_in_sentence)


# In[68]:


#split into multisentences
multiSentence = 'The world is changing every second and minute. It is best to evolve with it. Do not be left behind. Make a change'
splitMultipleSentence = multiSentence.split('.')
print(splitMultipleSentence)
#join sentences
joinToSentence = '$'.join(multiSentence)
print(joinToSentence)


# In[71]:


#concatenate 2 lists together
list_1 = ['My name is antetokumbo']
list_2 = ['I live in Toronto']
multiply_list1 = list_1 * 5
print(multiply_list1)
print(list_2 + list_2)
print(len(multiply_list1))


# In[73]:


#manipulate, sort, max, min numbered list
num_list = [34,5,678,1,0,32,67,90,12,4,3,8,567,3452,123456]
print(num_list)
sort_num = sorted(num_list)
print(sort_num)
print(min(sort_num))
print(max(sort_num))
print(len(sort_num))


# In[90]:


#nested number list
nested_list = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]
print(nested_list)
print(nested_list[2])
print(nested_list[1][3])
print(nested_list[1:3])
del(nested_list[4])  #delete list in position 4
print(nested_list)


# In[94]:


var_with_s = 'solutions, sundars, sabotage'
print([s for s in var_with_s if s == 's']) #print all the 's' in the list


# In[ ]:




