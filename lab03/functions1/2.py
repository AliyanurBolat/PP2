#2
def convert_temperature(x):
    celsius = (5 / 9) * (x - 32)
    return celsius
f = int(input())
s = convert_temperature(f)
print(s)

