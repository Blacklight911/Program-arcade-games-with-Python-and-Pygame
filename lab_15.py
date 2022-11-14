"""This lab 15 is demonstrates the operation of linear and binary search algorithms"""
import re


# Function to split apart words in a string and return them as a list
def split_line(str_line):
	return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', str_line)


# Function reading file and return list
def read_file(file, list_name):
	file = open(file)
	list_name = []
	for line in file:
		line = line.strip()
		list_name.append(line)
	file.close()
	return list_name


dictionary_list = []


# --- Linear search
def linear_search(name_list, key_name):
	i = 0
	while i < len(name_list) and name_list[i] != key_name:
		i += 1
		if i < len(name_list):
			pass
		else:
			print('Line', line_number,  'possible misspelled word:', word)


# --- Binary search
def binary_search(list_name, key_name):
	lower_bound = 0
	upper_bound = len(list_name) - 1
	found = False
	while lower_bound <= upper_bound and not found:
		middle_pos = (lower_bound + upper_bound) // 2
		if list_name[middle_pos] < key_name:
			lower_bound = middle_pos + 1
		elif list_name[middle_pos] > key_name:
			upper_bound = middle_pos - 1
		else:
			found = True
	if found:
		pass
	else:
		print('Line', line_number,  'possible misspelled word:', word)


dictionary_list = read_file('dictionary.txt', dictionary_list)
print('--- Linear Search ---')
alice_200_file = open('AliceInWonderLand200.txt')
words = ''
line_number = 1
for line in alice_200_file:
	words = split_line(line)
	for word in words:
		linear_search(dictionary_list, word.upper())
	line_number += 1
alice_200_file.close()

print('--- Binary search ---')
alice_200_file = open('AliceInWonderLand200.txt')
words = ''
line_number = 1
for line in alice_200_file:
	words = split_line(line)
	for word in words:
		binary_search(dictionary_list, word.upper())
	line_number += 1
alice_200_file.close()
