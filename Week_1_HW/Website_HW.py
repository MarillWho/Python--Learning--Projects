# Exercise 1
def results(k, r):
    sum = k + r
    sub = k - r
    mul = k * r

    print(sum, sub, mul)


results(10, 30)


# Exercise 2
def roll_number(x):
    my_list = [1, 2, 4, 6, 10, 15, 10, 24]

    if x in my_list:
        print(" Present")
    else:
        print(" Absent")


roll_number(16)


# Exercise 3
def numbers(f, u, c):
    print(max(f, u, c))


numbers(50, 5, 100)


# Exercise 4
def number(k):
    if k % 2 > 0:
        print(" This is odd. ")
    else:
        print(" This is even. ")


number(12)


# Exercise 5
def word(x):
    my_list = ["a", "e", "i", "o", "u"]
    vow = 0
    con = 0
    for i in range(len(x)):
        if x[i] in my_list:
            vow = vow + 1
    else:
        con = con + 1
    print(" Count of vowels", vow)
    print(" Count of consonants", con)


u = input(" Enter word: ")

word(u)


# Exercise 6
def number(fac):
    fact = 1
    while fac != 0:
        fact *= fac
        fac = fac - 1
    print(" Factorial is", fact)


fac = int(input(" Enter a number please: "))

number(fac)


# Exercise 7
def user(re):
    v = re.upper()
    print(v)


re = input(" Enter any word/letter: ").lower()

user(re)


# Exercise 8
def circles():
    r = int(input(" Enter radius: "))
    area = 3.14 * (r ** 2)
    print(area)


circles()
