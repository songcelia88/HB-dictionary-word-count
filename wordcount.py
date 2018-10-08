import sys

print("The arguments are: " , str(sys.argv))

word_counts = {}
punctuation = [",", ".", ":", ";", "?", "/", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=","{", "}", "[", "]", "'", '"']

filename = sys.argv[1]

with open(filename) as file:
	for line in file:
		line = line.rstrip()
		for mark in punctuation:
			line = line.replace(mark, "")


		word_lst = line.split(" ")

		# print(word_lst)
		for word in word_lst:
			word = word.lower()
			word_counts[word] = word_counts.get(word,0) + 1

print(word_counts)
#print(len(word_counts))