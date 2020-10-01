#!/usr/bin/env python
# coding: utf-8

# # Data Types
# 
# `> ` Numeric: int, float, complex <br>
# `> ` Text: Str <br>
# `> ` Boolean: bool <br>
# `> ` Sequence: list, tuple,range <br>
# `> ` Set: set, frozenset <br>
# `> ` Mapping: dict <br>
# `> ` Binary: bytes, bytearray, memoryview <br>


## order of arithmetic resolution
### Brackets, Exponential, Division, Multiplication, Addition, and Subtraction


print('| ! Hello world. ! |')


print('Good morning\nmy neighbours!')


varString = "This is gonna be a long ride"
print(varString)


type(varString)


###BEDMAS
print(2 - 5 * 9 + 6 / 4)



Int1 = 34
Int2 = 4
print(Int1 + Int2)
print(Int1 - Int2)
print(Int1 * Int2)
print(Int1 / Int2)
print(Int1 // Int2) #absolute value of division
print(Int1 % Int2)  #remainder of division
print(Int1 ** Int2) #exponential
type(Int1)


#Increment and Decrement
Num1 = 12
Num1 += 1
print(Num1)
Decrement = 12
Decrement -= 1
print(Decrement)


# float
Num2 = 34.79
print(Num2)
type(Num2)



# complex numbers
Num3 = 34 + 4j
print(Num3)
type(Num3)



#logical
print(10 < 11)
a = 34
b = 12
print(True and False)
print(True or False)
print(a!=b)


print(True and not False)
print(False and not True)


# Text conversion
letters = 'this letters are lower case'
print(letters.upper())

upperLetters = 'THIS ONES ARE UPPER'
print(upperLetters.lower())


# Rstrip removes space from the end ---> right strip
strip_Sentence = 'There is a space at the end '
print(strip_Sentence)
print(strip_Sentence.rstrip())


# lstrip removes space from the beginning ---> left strip
strip_sentence2 = ' There is a space at the beginning'
print(strip_sentence2)
print(strip_sentence2.lstrip())


# Example of Rstrip and Lstrip ---> remove particular character
percentnum = '500%'
percentnum2 = '$567'
random_characters = '######5557585858&&&&&&'

print(percentnum.rstrip('%'))
print(percentnum2.lstrip('$'))
print(random_characters.rstrip('&').lstrip('#'))


# mixedString[0:2] ---> system counting first three characters of
# mixedString variable starting from 0,1,2
mixedString = '10 People affected by corona'
no_of_people = mixedString[0:11]
rest_of_string = mixedString[3:]
part_of_string = mixedString[2:5]
print('number of people are: ', no_of_people)
print('number of people are: ', rest_of_string)
print('number of people are: ', part_of_string)


#output part of string
groupString = 'There are 50 states in america. Get that? '
states = groupString[5:30]
print(states)
print(groupString[:-2])



#output even numbers
numSeq = '123456789'
evenNums = numSeq[1::2]
print(evenNums)

#output odd numbers
print(numSeq[0::2])
print(numSeq[::2])


# concatnation of strings
firstName = 'Allen'
lastName = 'Antetokumbo'
fullName = firstName + ' ' + lastName
print(fullName)


#datatype conversion ----> int to string
age = 30
ageText = ('I am currently '+ str(age) + ' years old.')
print(ageText)

#text formatting
formatAge = '*Putting this text before* {0} #and this text after#'.format(ageText)
print(formatAge)


#string formatting
first = "Machine"
second = "Learning"
third = 'Training'
fourth = 'with python'
print('{0} {1} {2} {3} using jupyter'.format(first,second,third,fourth))

#concatnate and update text
firstName + ' ' + ageText
print(firstName)

