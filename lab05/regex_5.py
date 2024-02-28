import re
def stringMatch(text):
        patterns = 'a.*?b$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
s = str(input())
print(stringMatch(s))