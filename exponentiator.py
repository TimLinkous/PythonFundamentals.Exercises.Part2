def exponentiate(a, b):
    return a ** b
"""Function exponentiate is raising int a to the power of b"""


def raised_to_the_fourth_power(a):
    return exponentiate(a, 4)
"""taking the base value from exponentiate and raising to 
power of 4"""


square = lambda x : exponentiate(x,2)

cube = lambda y : exponentiate(y, 3)

print(square(2))
print(cube(2))
print(raised_to_the_fourth_power(2))