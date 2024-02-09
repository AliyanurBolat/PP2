n = [int(a) for a in input().split()]

def histogram(n):
    for num in n:
        print('*' * num)

histogram(n)
