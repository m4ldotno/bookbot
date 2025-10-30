from stats import get_book_text, get_num_words, get_num_chars, sort_chars

def main():
    print("=========== BOOKBOT ============")

    book_path="books/frankenstein.txt"
    book = get_book_text(book_path)
    print(f"Analyzing book found at {book_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {get_num_words(book)} total words")
    print(f"--------- Character Count -------")
    book_chars = get_num_chars(book)

    sorted_chars = sort_chars(book_chars)
    # print(f"Debug sorted_chars: {sorted_chars}")
    for dicts in sorted_chars:
        if dicts["char"].isalpha() is not True:
            continue
        else:
            print(f"{dicts["char"]}: {dicts["num"]}")
    

main()
