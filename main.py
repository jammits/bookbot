def get_book_text(filepath):

  with open(filepath) as file:
    file_contents = file.read()

    return file_contents


def word_count(text):
  words = text.split()
  return len(words)

def main():
 num_words = word_count(get_book_text("./books/frankenstein.txt"))

 print(f"{num_words} words found in the document")



main()