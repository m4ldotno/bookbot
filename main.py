from stats import get_book_text, get_num_words, get_num_chars, sort_chars

def main():
    import sys

    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("=========== BOOKBOT ============")
    book_path=sys.argv[1]
    book = get_book_text(book_path)
    print(f"Analyzing book found at {book_path}...")

    print(f"----------- Word Count ----------")
    print(f"Found {get_num_words(book)} total words")

    print(f"--------- Character Count -------")
    book_chars = get_num_chars(book)
    sorted_chars = sort_chars(book_chars)
    for dicts in sorted_chars:
        if dicts["char"].isalpha() is not True:
            continue
        else:
            print(f"{dicts["char"]}: {dicts["num"]}")
    print(f"============= END ===============")

main()
