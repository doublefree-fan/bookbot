from book_paths import FRANKENSTEIN_PATH_FILE

def count_characters(book):
    """
    Counts the number of chars in a given book
    Args:
        book (str): the text of the book
    Returns:
        chars (dict): str -> int containing the number of each lowered char
    Raises:
        Exception: if book is not provided (empty string or None)
    """
    if not book:
        raise Exception("book was not provided")
    chars = dict()
    lowercase_book = book.lower()
    for char in lowercase_book:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars

def count_words(book):
    """
    Counts the number of words in a given book
    Args:
        book (str): the text of the book
    Returns:
        int: the number of words in the book
    Raises:
        Exception: if the book is not provided (empty string or None)
    """
    if not book:
        raise Exception("book was not provided")
    return len(book.split())

def read_book(book_path):
    """
    Reads contents of a book file from the given the path
    Args:
        book_path: string path to the book file
    Returns:
        string: containing the entire book contents
    Raises:
        Exception: if book_path is empty
    """
    if not book_path:
        raise Exception("book not found")
    with open(book_path) as file:
        book = file.read()
        return book

def main():
    try:
        book = read_book(FRANKENSTEIN_PATH_FILE)
        book_words = count_words(book)
        book_chars_count = count_characters(book)
        print(book_words)
        for key in book_chars_count:
            print(f'"{key}": "{book_chars_count[key]}"')
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
