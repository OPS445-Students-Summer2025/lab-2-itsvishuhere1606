#!/usr/bin/env python3
# Author: Vishesh
# Author ID: vishesh1@myseneca.ca
# Date Created: 2025/05/21

import sys

if len(sys.argv) == 2:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer != 0:
    print(timer)
    timer = timer - 1

print("blast off!")
