# Brian's Question (e)
def characters():
    user = input(" Please enter a word: ")
    result = " "
    for letter in user:
        result = result + letter * 3
    return result


print(characters())
