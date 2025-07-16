def get_book_text(filepath):

  with open(filepath) as file:
    file_contents = file.read()

    return file_contents




def main():
  print(get_book_text("./books/frankenstein.txt"))




main()