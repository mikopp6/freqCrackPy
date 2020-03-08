#!/usr/bin/python
# -*- coding: utf-8 -*-


def main():
	
	file = open("message", "r")	
	message = file.read()
	file.close()

	oldchar = input("Input old char: ")
	newchar = input("Input new char: ")
	
	for character in message:
		if(character == oldchar):
			character = newchar


if __name__ == '__main__':
    # Call the main function when this script is executed
    main()