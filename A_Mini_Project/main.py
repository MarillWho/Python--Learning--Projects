class MainPart:

    def __init__(self, value: int):
        self.value = value

    def exception(self, value):
        value = self
        try:
            if value is int and value % 1 == 0:
                return True
        except ValueError:
            print("This is not a whole number, please try again.")


def main(self):
    odd = 0
    even = 0
    number = []
    user = self
    while user > 1:
        if user % 2 == 0:
            user = user / 2
            even = even + 1
            print(user)
            number.append(user)

        else:
            user = ((user * 3) + 1)
            odd = odd + 1
            print(user)
            number.append(user)

    question = input(" Please enter a number greater than 0: ")

    print(" The odd cycle " + str(odd) + " times.")
    print(" The even cycle " + str(even) + " times.")
    print(" The equation " + str((odd + even)) + " times.")
    print(" The highest integer reached was: " + (str(max(number))))


main(12)
