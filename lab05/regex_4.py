import re
def Match(text):
        x = '[a-z]+[A-Z]'
        if re.search(x, text):
                return 'Found a match!'
        else:
                return('Not mached!')
b = str(input())
print(Match(b))