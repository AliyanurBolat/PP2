n = [int(a) for a in input().split()]
def Unique(n):
    uniq = []
    for a in n:
        if a not in uniq:
            uniq.append(a)
    print(uniq)
    
c = Unique(n) 