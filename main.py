import os

characters_counted = {}
characters_counted_list = []

def main(book_path):

    name = get_book_name(book_path)
    book_text = get_book_text(book_path)
    num_words = word_counter(book_text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in {name}")
    print(" ")
    character_counter(book_text)
    print("--- End report ---")
    
    

def get_book_name(book_path):
    book_name = os.path.basename(book_path)
    return book_name

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_counter(file_contents):
    words = file_contents.split()
    return len(words)

def sort_on(characters_counted_dict):
        return characters_counted_dict["num"]

def character_counter(book_text):    
    book_text_lower = book_text.lower()
    for character in book_text_lower:
        if character.isalpha():  # Only count the character if it's in the alphabet
            if character in characters_counted:
                characters_counted[character] += 1
            else:
                characters_counted[character] = 1
    for name, num in characters_counted.items():
        ind_characters_dict = {"name": name, "num": num}
        characters_counted_list.append(ind_characters_dict)
    characters_counted_list.sort(reverse = True, key = sort_on)
    
    for dict in characters_counted_list:
        print(f"The {dict["name"]} character was found {dict["num"]} times")
    

    









    







main("/home/guy/workspace/github.com/GuyMitchy/Bookbot/books/frankenstein.txt")