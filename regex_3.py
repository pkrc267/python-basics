# -------------------------- Regex Dot-Star and the Caret/Dollar Characters --------------------------

import re
# we used ^ to negate regex,
# but we can use it in the beginning of regex to indicate a patter must start with given regex
# we can put a dollar to indicate a pattern must end with given regex

# -------------------------- Regex Caret/Dollar Characters --------------------------


print('~~~~~~~~~~~~~~~~~~~~ Starting with a pattern ~~~~~~~~~~~~~~~~~~~~')
regex = re.compile(r'^Hello')
print(regex.search('Hello fucking citizens. We start with Hello here.'))
print(regex.findall('Hello fucking citizens. We start with Hello here.'))

print('~~~~~~~~~~~~~~~~~~~~ Ending with a pattern ~~~~~~~~~~~~~~~~~~~~')
regex = re.compile(r'world$')
print(regex.search('because of your dumb ass its going to be the end of the world'))

print('~~~~~~~~~~~~~~~~~~~~ Starting & Ending with a pattern ~~~~~~~~~~~~~~~~~~~~')
regex = re.compile(r'^\d+$')  # start with digit, end with digit, have only digits in the middle
print(regex.search('1788791234'))
print(regex.search('1723t1723'))  # returns none because it has the alphabet 't' in the middle


# -------------------------- Regex Dot-Star Characters --------------------------

# Dot character class: .
# -- any character except for the new line
print('~~~~~~~~~~~~~~~~~~~~ Dot-Star ~~~~~~~~~~~~~~~~~~~~')
regex = re.compile(r'.*')
print(regex.findall('this is stupid and it will match everything except new line\n trust me I\'m not kidding'))

regex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(regex.findall('First Name: Stupid Last Name: Funk'))

regex = re.compile(r'<(.*)>')  # greedy search with the biggest matchable string pattern
print(regex.findall('<this is a game> of life bitch>'))

regex = re.compile(r'<(.*?)>')  # conservative search with the smallest possible match
print(regex.findall('<this is a game> of life bitch>'))


