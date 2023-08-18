# (a)
def number(k, r):
    sum = k + r

    if sum == 20 or k == 20 or r == 20:
        return True


    else:
        return False


print(number(2, 5))


# (b)
def letters(word):
    my = list(word)
    my[0] = my[0].upper()
    my[3] = my[3].upper()

    return "".join(my)


# (c)
def word(sentence):
    s = sentence.split()[::-1]
    w = []
    for i in s:
        w.append(i)
    print(" ".join(w))


word("tommy")


# (d)
def number(k):
    if 90 <= k <= 110 or 190 <= k <= 210:
        return True
    else:
        return False


print(number(92))


# (e)
def characters():
    user = input(" Please enter a word: ")
    result = " "
    for letter in user:
        result = result + letter * 3
    return result


print(characters())
