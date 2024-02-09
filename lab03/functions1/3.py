#3
def solve(numheads, numlegs):
    numrabbits = (numlegs - (numheads * 2)) / 2
    return numrabbits
legs = 94
heads = 35
rabbits = solve(heads, legs)
chicken = heads - rabbits
print("Rabbits:", rabbits)
print("Chicken:", chicken)
