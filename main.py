
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    total_characters = count_characters(text)
    print(f"The dictionary is {total_characters}")
# counting the amount of words in the book
def get_num_words(text):
    words = text.split()
    return len(words)

#getting the book file
def get_book_text(path):
    with open(path) as f:
        return f.read()

# counting how many time each character is in the book
def count_characters(text):
    lowered_string = text.lower()
    char_dict = {}
    for i in lowered_string:
        if i not in char_dict:
            char_dict[i]= 1
        else:
            char_dict[i] += 1
    return char_dict



main()

