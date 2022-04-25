spam = ['cat', 'bat']
print(spam)
spam = [['cat', 'bat'], [10, 20, 30]]
print(spam)
print(spam[0][1])

# reverse index for -ve indexing
spam = ['cat', 'bat', 'rat', 'fat']
print(spam)
print(spam[-1])
# this is called slicing:
print(spam[1:3])
# this will evaluate to new list value, so it will return a list

# trying bulk mutation
spam[1:] = [0]
print(spam)  # -> ['cat', 0]

# delete element from list using `del` statement
spam = ['cat', 'bat', 'rat', 'fat']
print(spam)
del spam[2]
print(spam)


# length of list
print(len(spam))

# List concatenation, replication
print(spam + spam)  # -> ['cat', 'bat', 'fat', 'cat', 'bat', 'fat']
print(spam * 3)  # -> ['cat', 'bat', 'fat', 'cat', 'bat', 'fat', 'cat', 'bat', 'fat']

# Type casting to list with 'list()' function
print(list('spam'))

# 'in' & 'not in' operators for checking element's presence
print('cat' in spam)
print('sat' not in spam)


# ------------ FOR LOOPS with Lists ------------

# range object
print(range(4))  # -> range(0, 4)
# make list from range
print(list(range(4)))  # -> [0, 1, 2, 3]
# make list in a range with custom step size
print(list(range(0, 100, 2)))

spam = list(range(0, 100, 2))

# using for loop with range
for i in range(4):
	print(i)

for i in range(len(spam)):
	print(str(i) + " : " + str(spam[i]))

# multiple assignment trick
spam = ['cat', 'bat', 'rat']
what, the, fuck = spam
print(what, the, fuck)

# swapping
a = 222
b = 333
a, b = b, a
print(a, b)

# index, append, insert
# append & insert are only list method and will not work for other datatypes
spam = ['cat', 'bat', 'rat']
spam.index('cat')  # if element not present, python returns an error
spam.append('cat')  # inserts element at the end
spam.insert(1, 'scat')
spam.index('cat')  # returns index of 1st occurence
spam.remove('cat')  # removes an element (1st occurence). If element not present, we get error
# list is modified inplace

# sort
# sorts in ASCII-betical order: uppercase letters come before lower case
# to sort in alphabetical order, pass key=str.lower in sort function
spam.sort(key=str.lower, reverse=False)

# if list has ints and strings, then sort will throw error because it does not know how to compare strings to integers

# List &  string work similarly, except LIST is mutable & String is immutable
# hence when we assign LIST to some other variable, we just pass it as reference
# So to actually make a copy of a LIST we need to make a deep copy of it
import copy
spam_copy = copy.deepcopy(spam)
spam_copy[2] = 'stuff'
# now we have  spam_copy  as separate list than  spam



