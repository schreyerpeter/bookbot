from stats import character_dict, count_words, print_results
import sys

def get_book_text(path_to_file='book.txt'):
    with open(path_to_file) as f:
        return f.read()

def main():
    print(sys.argv)
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    num_words = count_words(book_text)
    char_dict = character_dict(book_text)
    print_results(sys.argv[1], num_words, char_dict)


main()