# Website Question 5
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
