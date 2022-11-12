"""Read in a file from disk and put it in an array."""

file = open("AliceInWonderland200.txt")
name_list = []
for line in file:
	line = line.strip()
	name_list.append(line)
file.close()

# --- Linear search
KEY = "Morgiana the Shrew"
i = 0
while i < len(name_list) and name_list[i] != KEY:
	i += 1
	if i < len(name_list):
		print( "The name is at position", i)
	else:
		print('The name was not in the list.')

# --- Binary search
KEY = "Morgiana the Shrew";
LOWER_BOUND = 0
UPPER_BOUND = len(name_list) - 1
FOUND = False

# Loop until we find the item, or our upper/lower bounds meet
while LOWER_BOUND <= UPPER_BOUND and not FOUND:
	# Find the middle position
	MIDDLE_POS = (LOWER_BOUND + UPPER_BOUND) // 2
	# Figure out if we: move up the lower bound, or move down the upper bound, or we found what we are looking for.
	if name_list[MIDDLE_POS] < KEY:
		LOWER_BOUND = MIDDLE_POS + 1
	elif name_list[MIDDLE_POS] > KEY:
		UPPER_BOUND = MIDDLE_POS - 1
	else:
		FOUND = True

if FOUND:
	print( "The name is at position", MIDDLE_POS)

else:
	print( "The name was not in the list." )

