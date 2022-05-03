# -------------------------- RegEx Character Classes & the findall() method -------------------------- #

# findall gives us two kinds of outputs:
#  - list of strings (when there is 0 to 1 groups only in our regex)
#  - list of tuples, tuples contain strings for corressponding groups
import re

myString = ''' 123-444-2342 is a bullshit number
and so is 444-212-9392 alond with fucking 538-666-6969
'''

# regex without grouping
print('~~~~~~~~~~~~~~~~~~~~Regex without grouping~~~~~~~~~~~~~~~~~~~~')
phoneRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
print(phoneRegex.findall(myString))

# regex with groups
print('\n~~~~~~~~~~~~~~~~~~~~Regex with grouping~~~~~~~~~~~~~~~~~~~~')
phoneRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
print(phoneRegex.findall(myString))

# several character classes:
# \d - digits
# \D - anything other than digits
# \w - alphabets, digits and underscore
# \W - anything that's not alphanumeric or underscore
# \s - space, tab, newline
# \S - other than space, tab, newline

song = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a ' \
       'swimming, 6 geese a laying, 5 gold rings, 4 calling birds, 3 french hens, 2 turtle doves and a partridge in a ' \
       'pear tree walk into a bar. '

song_regex = re.compile(r'\d+\s\w+')
print('\n~~~~~~~~~~~~~~~~~~~~Items in xmas song~~~~~~~~~~~~~~~~~~~~')
print(song_regex.findall(song))

# Making our own regex character class
# syntax: r'[]'
vowel = re.compile(r'[aeiouAEIOU]')
print('\n~~~~~~~~~~~~~~~~~~~~Custom Vowel Regex~~~~~~~~~~~~~~~~~~~~')
print(vowel.findall('fucking bullshit that is a baby shit pig food'))

# not symbol: ^
vowel = re.compile(r'[^aeiouAEIOU\s]')  # anything that's not vowel or space
print('\n~~~~~~~~~~~~~~~~~~~~Custom !Vowel Regex~~~~~~~~~~~~~~~~~~~~')
print(vowel.findall('fucking bullshit that is a baby shit pig food'))

# multiple characters
vowel = re.compile(r'[aeiouAEIOU]{2}')  # anything that's not vowel
print('\n~~~~~~~~~~~~~~~~~~~~Custom Vowel multiple chars Regex~~~~~~~~~~~~~~~~~~~~')
print(vowel.findall('fucking bullshit that is a baby shit pig food'))

