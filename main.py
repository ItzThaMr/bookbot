
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

# counting the amount of words in the book
def get_num_words(text):
    words = text.split()
    return len(words)

#getting the book filee
def get_book_text(path):
    with open(path) as f:
        return f.read()





main()

