#1
def multiply(num):
    product = 1
    for i in num:
        product *= int(i)
    return product
l = input()
input_l = l.split()
print(multiply(input_l))

#2
def string_test(s):
    d = {"upper": 0, "lower": 0}
    for c in s:
        if c.isupper():
            d["upper"] += 1
        elif c.islower():
            d["lower"] += 1
        else:
            pass
    print(d["upper"])
    print(d["lower"])

s = str(input())    
string_test(s)

#3
def isPalindrome(string):
    left_pos = 0
    right_pos = len(string) - 1
    while right_pos >= left_pos:
        if not string[left_pos] == string[right_pos]:
            return False
        
        left_pos += 1
        right_pos -= 1
    return True
s = str(input())
print(isPalindrome(s))

#4
from time import sleep
import math

def delay(x, ms, *y):
    sleep(ms / 1000)
    return x(*y) 

t = int(input())
n = int(input())
print(delay(lambda num: math.sqrt(num), t, n))

#5
def all_true(t):
    return all(t)

my_tuple = (True, True, True, True)
print(all_true(my_tuple))

my_tuple = (True, True, False, True)
print(all_true(my_tuple))