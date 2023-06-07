# Brian's Question (c)
# unsure if I did this right, also ::-1 is a little confusing
def word(sentence):
    s = sentence.split()[::-1]
    w = []
    for i in s:
        w.append(i)
    print(" ".join(w))


word("tommy")
