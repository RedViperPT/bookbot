from stats import get_word_count, get_char_count, char_sort
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book_text = get_book_text(filepath)  
    num_chars = get_char_count(book_text)
    sorted_num_chars = char_sort(num_chars)

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {filepath}...')
    print('----------- Word Count ----------')
    get_word_count(book_text)
    print('--------- Character Count -------')
    for item in sorted_num_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()