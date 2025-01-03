
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    total_words = 0
    for word in file_contents.split():
        total_words += 1
    print(total_words)







main()

