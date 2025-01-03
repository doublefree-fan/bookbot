from book_paths import FRANKENSTEIN_PATH_FILE

def read_book(book_path):
    """
    Reads contents of a book file from the given the path.
    Args:
        book_path: string path to the book file
    Returns:
        string containing the entire book contents
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
        print(book)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
