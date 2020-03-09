#!/usr/bin/python

from collections import Counter

def main():

	encrypted_message = ""
	with open("message", encoding="utf-8") as f:
		for line in f:
			encrypted_message += line

	finnish_freq = ""
	with open("finnishFreq", encoding="utf-8") as f:
		for line in f:
			finnish_freq += line

	message_freq = Counter(encrypted_message)

	key = ""
	message = encrypted_message
	quit = False;

	while(quit==False):
		print("\n" + message)
		task = input("\nChange letter in format X=y, freq to print frequencies, \nquit to exit, reset to start over: ")
		if len(task)==3:
			oldchar = task[0]
			newchar = task[2]
			message = message.replace(oldchar,newchar)
			key = key + (oldchar + "=" + newchar + ", ")
		elif task=="freq":
			print("\nFrequencies in message ")
			print(message_freq)
			print("\nFrequencies in finnish language " + finnish_freq)
		elif task=="reset":
			message = encrypted_message;
		elif task=="quit":
			quit = True;
		else:
			print("\nInvalid input")
	
	print("\nOriginal encrypted message:\n" + encrypted_message)
	print("\nKeys for encryption: " + key)
	print("\nDecrypted message:\n" + message)



if __name__ == '__main__':
	# Call the main function when this script is executed
	main()
