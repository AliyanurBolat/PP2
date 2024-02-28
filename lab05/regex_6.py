import re
s = str(input())
print(re.sub("[ ,.]", ":", s))