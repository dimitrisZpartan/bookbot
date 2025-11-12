from stats import count_words, count_characters, sort_dict
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]

    num_words , file_contents = count_words(filepath)

    char_count = count_characters(file_contents)

    #print(char_count)

    final_dict = sort_dict(char_count) 

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for k, v in final_dict.items():
        print(f"{k}: {v}")
    print("============= END ===============")

main()