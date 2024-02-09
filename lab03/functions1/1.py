#1
def convert_grams(x):
    num= float(x)
    ounces = 28.3495231 * num
    return ounces
a = input()
result = convert_grams(a)
print(result)
