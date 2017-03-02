#!/usr/bin/python

import sys

# Use Euclid's algorithm to find the GCF

# Find the difference between two numbers
# Replace the larger number with the difference
# Repeat until both parameters are equal

def gcf(a, b):
	if a == b:
		return a
	elif a > b:
		return gcf(a-b, b)
	else:
		return gcf(b-a, a)

print gcf(int(sys.argv[1]), int(sys.argv[2]))