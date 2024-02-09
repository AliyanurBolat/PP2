word1 = str(input())
word2 = word1[::-1]
def Polindrome(word1):
    if word1 == word2:
        print('YES')
    else:
        print('NO')

g = Polindrome(word1)