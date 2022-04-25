# -------------------------- REGEX -------------------------- #
import re

# raw string compile(r'\d\d\d-\d\d\d-\d\d\d\d')


message = "this is bull shit number 641-158-1777, so fuck the number 641-158-1777 to repeat"
# define reg ex
phoneRegEx = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# take the matched object
mo = phoneRegEx.search(message)
# matched object has group() function which can return the text of the matching object
print(mo.group())

print(phoneRegEx.findall(message))  # finds all occurrences and makes a list of them

# -------------------------- REGEX Groups & Pipe character-------------------------- #
# parenthesis to mark out the groups
# they help to find out specific parts in the message
phoneRegEx = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneRegEx.search(message)
print("----------------------------")
print("group 1: " + str(mo.group(1)) + "-- group 2: " + str(mo.group(2)))

# pipe character to match one of several expressions
print("----------------------------")
batRegEx = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegEx.search('Batmobile is a stupid shit')
# mo = batRegEx.search('Batmotorcycle is a stupid shit')  # returns error because the 'none' is returned to 'mo'
# and 'none' does not have group() function
print(mo.group())  # equivalent to mo.group(0)
print(mo.group(1))
print("----------------------------")

# -------------------------- Repetition in RegEX Pattern + Greedy/Non-Greedy Matching -------------------------- #
# ? --> match preceding group 0 or 1 time
batRegEx = re.compile(r'Bat(wo)?man')
mo = batRegEx.search('the adventures of Batman')
print(mo.group())
mo = batRegEx.search('the adventures of Batwoman')
print(mo.group())
# mo = batRegEx.search('the adventures of Batwowoman')  # returns error as more than 1 repetition
# print(mo.group())

print("----------------------------")
phoneRegEx = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')  # this will check for first 3 number occurrence 0 or 1 time
mo = phoneRegEx.search(message)
print(mo.group(1))

print("----------------------------")
# how to check for '?' in our patter?
# just escape it using backslash \
regex = re.compile(r'dinner\?')
print(regex.search('wanna go for dinner?').group() is not None)

print("----------------------------")
# * --> match 0 or more time; Kleene closure
batRegEx = re.compile(r'Bat(wo)*man')
mo = batRegEx.search('the adventures of Batwowowowoman')
print(mo is not None)

print("----------------------------")
# + --> match 1 or more time; Positive closure; must have at least one occurrence
batRegEx = re.compile(r'Bat(wo)+man')
mo = batRegEx.search('the adventures of Batman')  # since no 'wo', this will return 'None'
print(mo is not None)

print("----------------------------")
# escaping ? * +
regex = re.compile(r'\+\*\?')
print(regex.search('I learnt about +*? regex syntax'))

print("----------------------------")
# exact number of matches
phoneRegEx = re.compile(r'(\d){3}-(\d){3}-(\d){4}')  # this will check for first 3 number occurrence 0 or 1 time
mo = phoneRegEx.search(message)
print(mo.group())


print("----------------------------")
# {x,y} --> x: at-least, y: at-most number of matches
# phoneRegEx = re.compile(r'(ha){,5}')  # same as {0,5}
phoneRegEx = re.compile(r'(ha){3,5}')  # this will check for first 3 number occurrence 0 or 1 time
mo = phoneRegEx.search('funny bullshit hahaha')
print(mo is not None)

print("----------------------------")
# ----- Greedy Match ----- #
# by default regex has greedy match mechanism
# meaning, it will match the longest possible string
phoneRegEx = re.compile(r'(\d){3,5}')
mo = phoneRegEx.search('1234567890')  # matches first occurring the longest pattern
print(mo.group())

# ----- Non-Greedy Match ----- #
# it will match the smallest possible string
# use '?' after the '{}' for it
phoneRegEx = re.compile(r'(\d){3,5}?')
mo = phoneRegEx.search('1234567890')  # matches first occurring the shortest pattern
print(mo.group())
