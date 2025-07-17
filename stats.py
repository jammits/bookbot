def word_count(text):
  words = text.split()
  return len(words)

def character_count(text):
  text_lower = text.lower()
  character = {}

  for ch in text_lower:
    if ch in character:
      character[ch] += 1
    else:
      character[ch] = 1

  return character


def sort_on(dict):
  return dict["num"]


def sorted_dict(dict):
  list_dict = []

  for key,val in dict.items():
    temp_dict = {}
    temp_dict["char"] = key
    temp_dict["num"] = val
    list_dict.append(temp_dict)

  list_dict.sort(key=sort_on, reverse=True)
  return list_dict