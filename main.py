def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    print(f"--- Begin report of {f.name}")
    print(f"{count_words(file_contents)} words found in the book\n")

    new_count = character_count(file_contents)

    for item in new_count:
        print(f"The '{item}' character was found {new_count[item]} times")
    print("--- End report ---")        

def count_words(book):
    return len(book.split())

def character_count(book):
    character_count_dict = {}

    for character in book.lower():
        if character.isalpha():  
            if character not in character_count_dict:
                character_count_dict[character] = 1
            else:
                character_count_dict[character] += 1

    character_count_dict = dict(sorted(character_count_dict.items(), key=lambda item: item[1], reverse=True))
    
    return character_count_dict

main()