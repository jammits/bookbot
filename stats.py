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