from book_paths import FRANKENSTEIN_PATH_FILE

def filter_non_letter_chars(chars_dict):
    """
    Filters an item based on the key being a letter from the alphabet
    Args:
        chars_dict (dict): a str -> int where the key is a character and the value is the number of occurences
    Returns:
        list[dict]: a list where each dict contains exactly one key-value pair (char: count)
    Raises:
        Exception: if the char_dict is an empty or None
    """
    if not chars_dict:
        raise Exception("no chars_dict was provided")
    list_of_chars_dict = []
    for char in chars_dict:
        if char.isalpha():
            list_of_chars_dict.append({
                char: chars_dict[char]
            })
    return list_of_chars_dict

def sort_by_frequency(char_dict):
    """
    Helper function to sort based on the number of occurences of a character
    Intended to be used as a key function for sorting
    Args:
        char_dict (dict): where the key is a character and the value the number of occurences
    Returns:
        int: the number of occurences
    Raises:
        Exception: if char_dict is empty or None
    """
    if not char_dict:
        raise Exception("no character dict provided")
    return (list(char_dict.values())[0])

def print_report(book):
    """
    Prints a formatted report of word count and character frequencies from a book.
    Args:
        book (str): path to the book file to analyze
    Returns:
        None: prints results to console
    Notes:
        Catches and prints any exceptions that occur during processing
    """
    try:
        contents = read_book(book)
        num_words = count_words(contents)
        num_chars = filter_non_letter_chars(count_characters(contents))
        num_chars.sort(key=sort_by_frequency, reverse=True)
        print(f"--- Begin report of {book} ---")
        print(f"{num_words} found in the document\n")
        for char_dict in num_chars:
            for key in char_dict:
                print(f"The '{key}' character was found {char_dict[key]} times")
        print("--- End report ---")
    except Exception as e:
       print(e)

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
    print_report(FRANKENSTEIN_PATH_FILE)

if __name__ == "__main__":
    main()
