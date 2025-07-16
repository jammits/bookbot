from stats import word_count, character_count

def get_book_text(filepath):

  with open(filepath) as file:
    file_contents = file.read()

    return file_contents


def main():
  num_words = word_count(get_book_text("./books/frankenstein.txt"))

  print(f"{num_words} words found in the document")

  num_characters = character_count(get_book_text("./books/frankenstein.txt"))

  for ch, val in num_characters.items():
    print(f"'{ch}': {val}")






main()