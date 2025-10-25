def get_book_text(path_to_file):
    book_strings = ""
    with open(path_to_file) as f:
        book_strings = f.read()
    return book_strings

def get_num_words(book_text):
    num_words = 0
    for word in book_text.split():
        num_words += 1
    return num_words

