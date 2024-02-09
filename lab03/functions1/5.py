from itertools import permutations

def Solve(word):
    print()
    list_of_perm = permutations(word)
    for perm in list(list_of_perm):
        print(''.join(perm))
        
word = str(input())
a = Solve(word)