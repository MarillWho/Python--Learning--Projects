# Website Question 6
def number(fac):
    fact = 1
    while fac != 0:
        fact *= fac
        fac = fac - 1
    print(" Factorial is", fact)


fac = int(input(" Enter a number please: "))

number(fac)
