import sys

def get_book_text():
    with open(sys.argv[1]) as f:
        file_contents = f.read()
    return file_contents

def word_count():
	book_text = get_book_text()
	words = book_text.split()
	return len(words)

def letter_count():
    book_text = get_book_text()
    lowercase_book = book_text.lower()
    
    alphabet_counts = {}
   
    for char in lowercase_book:
        if char in alphabet_counts:
            alphabet_counts[char] += 1
        else:
            alphabet_counts[char] = 1
    return alphabet_counts


def sort_on(alphabet_counts):
    return alphabet_counts["count"]

counts = letter_count()

def high_to_low():
    alphabet_counts = []
    for letter in counts:
        alphabet_counts.append({
            "letter": letter,
            "count": counts[letter]
        })

    alphabet_counts.sort(key=sort_on, reverse=True)
    return alphabet_counts


