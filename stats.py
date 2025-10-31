def get_book_text(path_to_file: str) -> str:
    book_strings = ""
    with open(path_to_file, encoding="utf-8-sig") as f:
        book_strings = f.read()
    return book_strings

def get_num_words(book_text: str) -> int:
    num_words = 0
    for word in book_text.split():
        num_words += 1
    return num_words

def get_num_chars(book_text: str) -> int:
    num_characters = {}
    for word in book_text.split():
        for char in word:
            char = char.lower()
            if char not in num_characters:
                num_characters[char] = 0
            num_characters[char] += 1
    return num_characters

def sort_on(items: dict) -> int:
    return items["num"]

def sort_chars(char_dict: dict) -> list:
    sorted_dicts = []
    for item in char_dict:
        sorted_dicts.append(
            {"char": item, "num": char_dict[item]}
        )
    sorted_dicts.sort(reverse=True, key=sort_on)
    return sorted_dicts
