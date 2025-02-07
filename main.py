def main():
    with open("books/frankenstein.txt") as f:
        contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{num_words(contents)} words found in the document\n")
        characters = num_characters(contents)
        sorted_characters_by_occurence = sorted(characters.items(), key=lambda x:x[1], reverse=True)
        for c in sorted_characters_by_occurence:
            if c[0].isalpha():
                print(f"The '{c[0]}' character was found {c[1]} times")
        print("--- End report ---")

def num_words(s : str) -> int:
    return len(s.split())

def num_characters(text : str) -> {str, int}:
    d = {}
    for letter in text:
        try:
            d[letter.lower()] += 1
        except KeyError:
            d[letter.lower()] = []
            d[letter.lower()] = 1
    return d

def dict_sorter(dict):
    return dict.key

main()