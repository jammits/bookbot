import sys


from stats import word_count, character_count, sorted_dict

def get_book_text(filepath):

  with open(filepath) as file:
    file_contents = file.read()

    return file_contents


def main():

  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  else:
    file_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    num_words = word_count(get_book_text(file_path))

    print(f"Found {num_words} total words")

    num_characters = character_count(get_book_text(file_path))

    print("--------- Character Count -------")
    sorted_list = sorted_dict(num_characters)

    for item in sorted_list:
      if item["char"].isalpha():
        print(f"{item["char"]}: {item["num"]}")


    print("============= END ===============")




main()