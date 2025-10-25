from stats import get_book_text, get_num_words, get_num_chars

def main():
    frankenstein = get_book_text("books/frankenstein.txt")
    frankenstein_words = get_num_words(frankenstein)
    frankenstein_chars = get_num_chars(frankenstein)

    print(f"Found {frankenstein_words} total words")
    print(frankenstein_chars)

main()
