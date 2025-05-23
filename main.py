from stats import get_num_words, get_num_characters, get_sorted_characters_by_count


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()


def main():
    book_path = "./books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    num_characters = get_num_characters(book_text)
    sorted_characters = get_sorted_characters_by_count(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_characters:
        if type(item["char"]) == str and item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


main()
