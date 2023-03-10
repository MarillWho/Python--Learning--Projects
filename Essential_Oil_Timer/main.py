import time
import os

print("Essential Oil Diffuser Timer")

#listing essential oil choices
print("Please choose what scent to diffuse.")
input("Lavender, Sandalwood or Eucalyptus: ")

#putting in number of drops for recommended run time
input("How many drops would you like of the scent? ")
print("The recommended is between 3 to 5 drops.")


#defined input
user_input = input("Would you still like to continue with your choice? ")

#made lists for if else to work
yes_list = ["yes", "yea", "yeah", "yup", "y"]
no_list = ["no", "nah", "nope", "n"]

#defined drops
if user_input in yes_list:
    print("Alright, let's continue.")

else:
    drops = input("How many drops then? ")

#importing time and doing countdown

def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        os.system("cls")
        print(timer, end="\n")
        time.sleep(1)
        t -= 1

    print("Diffusing ended!!")

#User can insert time in seconds here
print("How long would you like the diffuser to run? ")

t = input("Enter the time in seconds: ")

countdown(int(t))



