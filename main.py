import string

def count_chars(book):    
    d = dict.fromkeys(string.ascii_lowercase, 0)
    for word in book.lower().split():
        for char in word:
            if char in d.keys():
                d[char] = d[char] + 1
    d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    for char in d.keys():
        print("The '", char, "' character was found ", d[char], " times")

def count_words(book):
    words = book.split()
    print(str(len(words)) + " words found in the document\n\n")

def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
        print("--- Begin report of ", book_path, " ---\n")
        count_words(file_contents)
        count_chars(file_contents)
        print("--- End report ---")

if __name__ == '__main__':
    main()
