from stats import word_count, char_count

def analyze_book():
    def get_book_text(filepath):
        with open(filepath, encoding='utf-8') as file:
            return file.read()

    book_path = 'books/frankenstein.txt'  # relative path to book's text file
    book_text = get_book_text(book_path)
    wc = word_count(book_text)
    cc = char_count(book_text)  
    return wc, cc

if __name__ == '__main__':
    wc, cc = analyze_book()
    print(f'Found {wc} total words')
    print(f'Character counts: {cc}')