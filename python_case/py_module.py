#!/usr/bin/python
# Filename: py_module.py
import sys

print 'The commadn line arguments are:'

for i in sys.argv:
	print i

print '\n\nThe PYTHONPATH is', sys.path, '\n'
