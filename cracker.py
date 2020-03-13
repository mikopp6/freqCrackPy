#!/usr/bin/python

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"

def main():

	with open("message", encoding="utf-8") as f:
		encrypted_message = ""
		for line in f:
			encrypted_message += line
	totalcharacters = len(encrypted_message) - encrypted_message.count(' ')
	message_freq = {}
	for k in alphabet:
		amount = encrypted_message.count(k)
		message_freq[k] = round(amount/totalcharacters*100, 2)

	sorted_message_freq = {}
	for k in sorted(message_freq, key=message_freq.get, reverse=True):
		sorted_message_freq[k] = message_freq[k]
	
	with open("finnishFreq", encoding="utf-8") as f:
		finnish_freq = {}
		for line in f:
			letter,count = line.split('=')
			finnish_freq[letter] = float(count)

	sorted_finnish_freq = {}
	for k in sorted(finnish_freq, key=finnish_freq.get, reverse=True):
		sorted_finnish_freq[k] = finnish_freq[k]

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
			print("\nFrequencies in message:")
			print(sorted_message_freq)
			print("\nFrequencies in finnish language:")
			print(sorted_finnish_freq)
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