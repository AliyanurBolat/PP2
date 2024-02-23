import math

#1
a = int(input())
r = math.radians(a)
print(r)
print()

#2
h = int(input('Height: '))
frist_v = int(input('Base, first value: '))
second_v = int(input('Base, second value: '))
m = (frist_v + second_v) / 2
area = m * h
print(area)
print()

#3
n_sides = int(input("Input number of sides: "))
s_length = int(input("Input the length of a side: "))
p_area = round(n_sides * (s_length ** 2) / (4 * math.tan(math.pi / n_sides)))
print("The area of the polygon is:", p_area)
print()

#4
l = int(input('Length of base: '))
h_l = int(input('Height of parallelogram: '))
s = l * h_l
print(s)