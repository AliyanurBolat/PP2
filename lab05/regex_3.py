import re
def StringMatch(text):
        pattern = '^[a-z]+_[a-z]+$'
        if re.search(pattern,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
s = str(input())
print(StringMatch(s))