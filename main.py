from stats import count_words, count_chars, dict_sort
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book = get_book_text(file_path)
    word_count = count_words(book)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words") 
    
    char_dict = count_chars(book)
    sorted_dict = dict_sort(char_dict)

    print("--------- Character Count -------")
    for dict in sorted_dict:
        if dict["char"].isalpha():
            print(f"{dict['char']}: {dict['num']}")
 
    print("============= END ===============")

main()
