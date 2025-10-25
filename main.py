from stats import get_book_text, get_num_words

def main():
    frankenstein = get_book_text("books/frankenstein.txt")
    print(f"Found {get_num_words(frankenstein)} total words")

main()
