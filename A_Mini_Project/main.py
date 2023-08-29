import csv
import sys
class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("logfile.log", "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass
sys.stdout = Logger()

# class with function for output sequence
class MainPart:
    even = 0
    odd = 0
    a = []

    def __init__(self):
        self.num = input(" Please enter a number: ").split()
        mark = False
        while not mark:
            try:
                for number in self.num:
                    if int(number) > 0:
                        mark = True
                    else:
                        print(" That isn't a positive number. Please try again. ")
                        mark = True
                        pass
            except ValueError:
                print(" That is not an integer. Please try again. ")
                mark = True
                pass
# function for outputting cycles/times ran
    def main(self):
        for this in self.num:
            print(" You have entered: " + this)
            try:
                while int(this) > 1:
                    if int(this) % 2 == 0:
                        this = int(this) / 2
                        MainPart.even += 1
                        MainPart.a.append(this)

                    else:
                        this = ((int(this) * 3) + 1)
                        MainPart.odd += 1
                        MainPart.a.append(this)

                print(MainPart.a)
                print(" The odd cycle ran " + str(MainPart.odd) + " times.")
                print(" The even cycle ran " + str(MainPart.even) + " times.")
                print(" The equation ran " + str((MainPart.odd + MainPart.even)) + " times.")
                print(" The highest integer reached was: " + (str(max(MainPart.a))))

            except ValueError:
                continue

# created csv with row for each
    with open("output_results.csv", "w", newline="") as file:
        writer = csv.writer(file)
        rows = [[data] for data in str(a)]
        writer.writerow(["Odd Cycle", " Even Cycle", " Equation Ran", " Highest Integer"])
        writer.writerow(rows)

hi = MainPart()
hi.main()