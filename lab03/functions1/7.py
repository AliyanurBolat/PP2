def has33(n):
    for i in range(len(n) - 1):
        if n[i] == 3 and n[i + 1] == 3:
            return True
    return False
    
a = input()
a_list = [int(n) for n in a.split()]
result = has33(a_list)
print (result)