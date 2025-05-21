#!/usr/bin/env python3


#print('Hi ' + name + ', you are ' + str(age) + ' years old.')
#colour = input("Type in a colour and press enter: ")
#print(colour)
#print('The colour I typed in is: ' + colour)

import sys

name = sys.argv[1]
age = int(sys.argv[2])

print(f"Hi {name}, you are {age} years old.")

