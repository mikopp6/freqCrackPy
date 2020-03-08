#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import Counter

alphabet = 'abcdefghijklmnopqrstuvwxyzåäö'

def main():
	
	file = open("message", "r")	
	message = file.read()
	file.close()

	print '\n' + message + '\n'
	freq = Counter(message)
	print freq


if __name__ == '__main__':
    # Call the main function when this script is executed
    main()