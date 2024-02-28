import re
def textMatch(text):
        pattern = 'ab{2,3}'
        if re.search(pattern,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
a = str(input())
print(textMatch(a))