def main():
    char_count_dict = {}
    list_of_dicts = []
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lowered_string = file_contents.lower()
        
        words = lowered_string.split()
        
        for char in lowered_string:
            if char in char_count_dict:
                char_count_dict[char] += 1
            else:
                char_count_dict[char] = 1
        list_of_dicts =[{char: count} for char, count in char_count_dict.items()]
        #print(char_count_dict)
        #print(list_of_dicts)
        list_of_dicts.sort(reverse=True, key=lambda d: list(d.values())[0])
        #print(list_of_dicts)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(words)} words found in the document")
        print()
        print()
        for d in list_of_dicts:
            for key, value in d.items():  # Each dictionary has only one key
                if key.isalpha():
                    print(f"The '{key}' character was found {value} times")
                #else:
                #    print(f"Key '{key}' is not an alphabetic character.")
        print("--- End report ---")

        

main()