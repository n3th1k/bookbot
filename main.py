import sys

from stats import word_count, char_count, sort_on

def analyze_book(book_path):
    def get_book_text(filepath):
        with open(filepath, encoding='utf-8') as file:
            return file.read()

    book_text = get_book_text(book_path)
    wc = word_count(book_text)
    cc = char_count(book_text)
    sorted_cc = sort_on(cc)
    return book_path, wc, sorted_cc

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    book_path_arg = sys.argv[1]
    book_path, wc, sorted_cc = analyze_book(book_path_arg)

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {book_path}...')
    print('----------- Word Count ----------')
    print(f'Found {wc} total words')
    print('--------- Character Count -------')
    for entry in sorted_cc:
        ch = entry['char']
        if not ch.isalpha():
            continue
        print(f'{ch}: {entry["num"]}')
    print('============= END ===============')