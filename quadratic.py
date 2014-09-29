#!/usr/bin/env python

import sys

def usage():
    print "This calculates the square root of a given number"
    print sys.argv[0] , "<number>"

if len(sys.argv) != 2:
    usage()
    sys.exit(1)

number = int(sys.argv[1])
quad = number**2

print quad
