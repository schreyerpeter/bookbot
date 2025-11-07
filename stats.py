def count_words(text):
    words = text.split()
    return len(words)

def character_dict(text):
    characters = list(text)
    dict_chars = {}
    for char in characters:
        if char.isalpha() == False:
            continue
        elif char.lower() in dict_chars:
            dict_chars[char.lower()] += 1
        else:
            dict_chars[char.lower()] = 1
    return dict_chars

def sort_on(items):
    return items["num"]

def sorted_dict_list(unsorted_dict):
    dict_list = []
    for key in unsorted_dict:
        dict_list.append({"char": key, "num": unsorted_dict[key]})
    dict_list.sort(key=sort_on, reverse=True)
    return dict_list

def print_results(book_path, word_count, char_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_dict_list(char_dict):
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")