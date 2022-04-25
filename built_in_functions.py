import random
import sys
import pyperclip as pc

# from random import *

print(random.randint(1, 20))  # random integer between a range


# we can install 3rd party programs using `pip3`
# lets try pyperclip, to copy and paste, to & from clipboard

pc.copy('Hello World!')
print(pc.paste())

sys.exit()  # exit the program
