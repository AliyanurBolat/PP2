#1
def gensquares(N):
    for i in range(N): 
        yield i**2
        
a = int(input())
for x in gensquares(a + 1):
    print(x)
print()
    
#2
def Mygenerator(n): 
    for i in range(n+1): 
        if i % 2 == 0: 
            yield str(i) 
 
c = int(input()) 
number = Mygenerator(c) 
print(",".join(number))
print()

#3
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
for number in divisible_by_3_and_4(n):
    print(number, end=" ")
print()

#4
def squares(a, b):
    for num in range(a, b+1):
        yield num ** 2

print()
d = int(input())
b = int(input())
for square in squares(d, b):
    print(square)
print()

#5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

x = int(input())
for number in countdown(x):
    print(number)
