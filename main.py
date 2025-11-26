import sys

if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

from stats import get_book_text, word_count, letter_count, high_to_low, sort_on

print(f"""
============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {word_count()} total words.
--------- Character Count -------""")
sorted_letters = high_to_low()
for letter_info in sorted_letters:
	letter = letter_info["letter"]
	count = letter_info["count"]
	if letter.isalpha():
		print(f"{letter}: {count}")
print("============= END ===============")



