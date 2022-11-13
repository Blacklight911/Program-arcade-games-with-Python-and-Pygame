import re

# Function to split apart words in a string and return them as a list


def split_line(line):
	return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def read_file(file, list_name):
	file = open(file)
	list_name = []
	for line in file:
		line = line.strip()
		list_name.append(line)
	file.close()
	return list_name


dictionary_list = []
key = 'Morgiana the Shrew'


# --- Linear search
def linear_search(name_list, key_name):
	key_name = 'Morgiana the Shrew'
	i = 0
	while i < len(name_list) and name_list[i] != key_name:
		i += 1
		if i < len(name_list):
			print('The name is at position', i)
		else:
			print('The name was not in the list.')


# --- Binary search
def binary_search(list_name, key_name):
	lower_bound = 0
	upper_bound = len(list_name)-1
	found = False

	while lower_bound <= upper_bound and not found:
		# Find the middle position
		middle_pos = (lower_bound + upper_bound) // 2
		# Figure out if we: move up the lower bound, or move down the upper bound,
		# or we found what we are looking for.
		if list_name[middle_pos] < key_name:
			lower_bound = middle_pos + 1
		elif list_name[middle_pos] > key_name:
			upper_bound = middle_pos - 1
		else:
			found = True

	if found:
		print('The name is at position', middle_pos)
	else:
		print('The name was not in the list.')


dictionary_list = read_file('dictionary.txt', dictionary_list)
print(dictionary_list)
print('--- Linear Search ---')
