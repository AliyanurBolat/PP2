import re
s = str(input())
print(re.findall('[A-Z][^A-Z]*', s))