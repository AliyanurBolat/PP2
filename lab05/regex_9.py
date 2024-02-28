import re
def capital_words_spaces(text):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", text)
s = str(input())
print(capital_words_spaces(s))