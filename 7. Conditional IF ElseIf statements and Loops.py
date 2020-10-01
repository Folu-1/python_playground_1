#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Conditional statements
# Branching out programming
# IF......ELSE
#IF.....ELIF.....ELSE


# In[1]:


#if conditional statements
score = int(input('Please enter an integer ')) 
if score < 0:
    print('You have entered a negative number')
elif score == 0:
    print('You have entered the number ZERO.')
elif score == 1:
    print('You have entered the number ONE.')
else:
    print('Eureka!, your entered value is more than 1. The value is ', score) #+ str(score))


# In[2]:


##### multiple if statements
#use "else:" if there are "elif" in the conditional statements
score = int(input('Please enter an integer ')) 
cutoff = 75
passmark = 60

if score >= cutoff:
    print('Congratulations, you have passed the test with a distinction.')
if score >= passmark and score < cutoff:
    print('Congratulations, you have passed the test')
if score < passmark:
    print('Sorry!, you failed the test')
if score == 100:
    print('Congratulations, you have earned a perfect score.')
elif 76 <= score < 100:
    print('Congratulations, you are intelligent.')
elif 60 <= score < cutoff:
    print('Your score is in the 60th percentile.')
else:
    print('You need to work hard.')


# In[3]:


#if conditional statements with strings
string1 = 'Mohindra works for Microsoft'
if 'Microsoft' in string1:
    print('Word ---> Microsoft found in variable.')
string2 = 'The covid situation in the world right now is crazy'
if 'situation' in string2:
    print('issue - situation')


# In[4]:


#put indentation into consideration for IF conditional statements
num = int(input('Enter an integer number '))
if num%2 == 0:
    print('You just entered an even number')
    if num%10 == 0:
        print('Divisible by 10')
    else:
        print('Not divisible by 10')
else:
    print('You just entered an odd number')
    if num%3 == 0:
        print('Divisible by 3')
    else:
        print('Not divisible by 3')


# In[5]:


if None:
    print('This statement will not execute')
else:
    print('This statement appears because it is not none')


# In[6]:


if True:
    print('This statement will always execute')
else:
    print('This statement appears because it is False')


# # Loops 
# FOR Loop<br>
# WHILE LOOP<br>
# RANGE()

# In[7]:


#for loop
#for i in fruits ---> i = individual values in the main varaible
fruits = ['Apple', 'Orange', 'Banana']
for i in fruits:
    print(i, len(i))


# In[12]:


#using range function in loop
for i in range(0,20):
    print(i)


# In[15]:


#using range function in loop
#with increment
for z in range(0,50,5):
    print(z)


# In[24]:


#for loop in a string
string = 'Once upon a time.'
for letters in string:
    print(letters)


# In[32]:


#Find the output
string1 = ''
for i in range(0,9):
    if i<5:
        string1 += '* '
        print(string1)
    elif i>4:
        string1 = string1[:-2]
        print(string1)


# In[34]:


#for loop count letters in string
#enumerate --> loop through variable content and index position
string = 'Once upon a time.'
for n,letters in enumerate(string):
    print(n,letters)


# In[39]:


#for loop to find even and odd numbers 
nums = '0123456789'
even_num = ''
odd_num = ''
#
#for det_num in nums:
#    if int(det_num)%2 == 0:
#        even_num = det_num
#        print(det_num + ' is an even number.')
#    else:
#        odd_num = det_num
#        print(det_num + ' is an odd number.')
for n_numbers in nums:
    if int(n_numbers)%2 == 0:
        even_num += n_numbers
    else:
        odd_num += n_numbers
print('All evens are : ' + even_num + ' & All odds are : ' + odd_num)


# In[42]:


#loop through inventories
list_of_inventories = ['Apple', 'Banana', 'Potato', 'Mango', 'Onion', 'paste']
fruits = ['Apple', 'Banana', 'Mango', 'Orange', 'Strawberry']
vegetables = ['Potato', 'Onion', 'Cucumber', 'Celery']

#count fruits in the inventory list
count_fruits = 0
##count vegetables in the inventory list
count_vegetables = 0

for item in list_of_inventories:
    if item in fruits:
        count_fruits += 1
        print('This item ' + item + ' is present in the inventory as a fruit.')
    elif item in vegetables:
        count_vegetables += 1
        print('This item ' + item + ' is present in the inventory as a vegetable.')
    else:
        continue
print(count_fruits)
print(count_vegetables)


# In[44]:


#for loop to split sentence
#Split a string into a list where each word is a list item:
sentence = 'Hello my dear friend.'
for word in sentence.split():
    print(word)


# In[47]:


#sentence check
#startswith() ---> Check if the string starts with
string_check = '#covid-19 #virus is #causing the world #alot.'
for word in string_check.split():
    if word.startswith('#'):
        print(word[1:])


# In[59]:


#dictionary --> key value pairs data
#loop through key/value pairs
#items() ---> Return the dictionary's key-value pairs:
students = {1:['Tolu', 34], 2:['Funmi', 25], 3:['Dele', 20]}
print(type(students))
for key, value in students.items():
    print(key,value)
for key in students.keys():
    print(key)
for key in students.values():
    print(value)
count = 0
for key, value in students.items():
    if value[1] < 25:
        count += 1
print(count)


# In[66]:


#while loop
#fibonacci series
n=50
a,b = 0,1
while a < n:
    print(a, end = ' ')
    a,b = b, a+b


# In[ ]:




