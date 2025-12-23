def count_words(book):
    words = book.split()
    word_count = len(words)
    return word_count

def count_chars(book):
    char_dict = {}
    for c in book.lower():
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict

def sort_on(items):
    return items["num"]


def dict_sort(dict):
    dict_list = []
    for key, value in dict.items():
        dict_list.append({"char": key, "num": value})

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
