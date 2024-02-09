def reverse(i):
    sentence = ''
    i = i[-1::-1]
    for j in i:
        sentence = sentence + j 
    print(sentence)
    
w = input()
result = reverse(w)
print(result)