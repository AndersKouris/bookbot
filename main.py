def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text()
    print(book_text)

def word_count():
	frankenstein_book = get_book_text()
	words = frankenstein_book.split()
	return len(words)

from stats import word_count

print("Found", word_count(), "total words")