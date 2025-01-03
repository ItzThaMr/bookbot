
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    
    total_characters = count_characters(text)
    ordered_dict = sort_by_value(total_characters)
    print(f"--- Begin report of {book_path}---")
    print(f"There have been a total of {num_words} words found in the document")
    for i in ordered_dict:
        if ordered_dict[i] == 1:
            print(f"The '{i}' character was found {ordered_dict[i]} time")
        else:
            print(f"The '{i}' character was found {ordered_dict[i]} times")
    print("--- End report ---")


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

def sort_by_value(char_dict):
    sorted_dict =dict(sorted(char_dict.items(), key=lambda item:item[1], reverse= True))       
    return sorted_dict

main()

