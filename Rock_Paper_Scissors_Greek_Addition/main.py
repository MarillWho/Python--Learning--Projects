# import for random & time
import time
import random

# intro
print("Rock, Paper & Scissors Greek God/Goddesses Addition!")
time.sleep(0.75)

# informing user of choices
print("These are your choices: Athena, Hermes, Apollo, Hecate & Hephestus.")
time.sleep(0.75)

# defining variables and making a list
a1 = [" She outsmarts Hephestus. ", " She bores Apollo to death. ", " She causes Athena's phasmaphobia. ",
      " He out talks Athena. "]
h1 = [" He outruns Hecate. ", " He out talks Athena. ", " He is blinded by Apollo. ",
      " He can't run anymore, Hephestus broke his shoes. "]
hp1 = [" He burns the witch, Hecate.  ", " He breaks Hermes' shoes. ", " He is lulled asleep by Apollo. ",
       " He is outsmarted by Athena. "]
hc1 = [" She contributed to Athena's phasmophobia. ", " She vexes Apollo. ", " She is burnt to death by Hephestus. ",
       " She is outrunned by Hermes. "]
ap1 = [" He blinds Hermes. ", " He lulls Hephestus to sleep. ", " He is vexed by Hecate. ",
       " He is bored to death by Athena. "]

# dictionary
gods = {
    "athena": {"hephestus": a1[0], "apollo": a1[1], "hecate": a1[2], "hermes": a1[3]},
    "hermes": {"hecate": h1[0], "athena": h1[1], "apollo": h1[2], "hephestus": h1[3]},
    "hephestus": {"hecate": hp1[0], "hermes": hp1[1], "apollo": hp1[2], "athena": hp1[3]},
    "hecate": {"athena": hc1[0], "apollo": hc1[1], "hephestus": hc1[2], "hermes": hc1[3]},
    "apollo": {"hermes": ap1[0], "hephestus": ap1[1], "hecate": ap1[2], "athena": ap1[3]}
}
# tried implementing who won in a set of 3 games not working
# running a loop
while True:
    user = input("Enter your choice: ").lower()
    possible = ("athena", "hermes", "hephestus", "hecate", "apollo")
    computer = random.choice(possible)
    try:
        print(" You selected : " + user.title())
        time.sleep(0.75)
        print(" The computer selected : " + computer.title())
        time.sleep(0.75)
        print(" The outcome..." + gods[user][computer])

        if user == computer:
            print(" Tie. ")
        elif gods[user][computer]:
            print(" You won!! ")
        else:
            print(" You lose. ")
    except:
        print("Sorry, that is not a choice.")
        time.sleep(0.75)

        # play again function
        user_input = input("Would you like to continue to play another round? ").lower()
        yes_list = ["yes", "yea", "yeah", "yup", "y"]
        if user_input in yes_list:
            continue
        else:
            break
# dev notes
# add 2 out of 3 best game
# clean up code
# play again function
