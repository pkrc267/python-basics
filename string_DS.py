spam = "this is bull shit"
print(spam.isupper())
print(spam.islower())
print(spam.upper())
print(spam.lower())
spam = spam + ". Fuck this Shit  42"
print(spam.isalnum())
print(spam.isascii())
print(spam.capitalize())
print(spam.startswith('t'))

print(spam.split('i'))
print(spam.strip('fthi2'))
print(spam.replace('this', 'that', 1))
