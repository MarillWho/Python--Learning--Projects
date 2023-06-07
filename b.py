# Brian's Question (b)
def letters(word):
    my = list(word)
    my[0] = my[0].upper()
    my[3] = my[3].upper()

    return "".join(my)