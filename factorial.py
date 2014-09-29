#!/usr/bin/env python

import sys

def usage():
  print "This program calculates the factorial of a given number"
  print sys.argv[0] , "<number>"

if len(sys.argv) != 2:
  usage()
  sys.exit(1)

number = int(sys.argv[1])

factorial = 1
for i in range (1, number+1):
	factorial *= i

print factorial
