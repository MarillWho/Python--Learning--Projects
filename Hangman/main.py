import random
import time
from word_list import words
import string

print(" Korean Artists & Groups Hangman! ")


# to choose words randomly
def select(words):
    wran = random.choice(words)
    while '-' in wran or ' ' in wran:
        wran = random.choice(words)

    return wran.upper()


def the_game():
    word = select(words)
    letters = set(word)
    alpha = set(string.ascii_uppercase)
    guess = set()

    lol = True
    # tries left, letters used and to guess letters
    tries = 6
    print(display(tries))
    while len(letters) > 0 and tries > 0:
        print(" You have", tries, "tries!\n Also, these are the letters that have been used: ", ''.join(guess))
        time.sleep(0.90)
        list = [letter if letter in guess else '_' for letter in word]
        print(" Current letters are: ", ' '.join(list))
        time.sleep(0.90)
        user = input(" Please type a letter: ").upper()

        # if elif else for when a letter is used or something else is typed in
        if user in alpha - guess:
            guess.add(user)
            if user in letters:
                letters.remove(user)
            else:
                tries = tries - 1
                print(" Err, no this letter isn't it. ")
                print(display(tries))
                time.sleep(0.90)

        elif user in guess:
            print(" Please try another letter :) already used this one! ")
            time.sleep(0.90)
        else:
            print("Bzzzt...invalid. Try again! ")
            time.sleep(0.90)

    if tries == 0:
        print(" Oh no!! There are no more tries.\n The artist or group name was", word)
        time.sleep(0.90)
    else:
        print(" Yay!! You got it right it was", word, "!")
        time.sleep(0.90)

    # tried using break, didn't work
    yes_list = ["yes", "yea", "yeah", "yup", "y"]
    user_input = input(" Would you like to continue to play another round? ").lower()
    if user_input in yes_list:
        the_game()
    else:
        exit()


# entered hangman display
def display(tries):
    stages = ["""
                            ------
                            |    |
                            |    O
                            |   -\-
                            |    |  
                            |   / /
                            -
                    """,
              """
                            ------
                            |    |
                            |    O
                            |   -\-
                            |    |
                            |   /
                            -
                    """,
              """
                            ------
                            |    |
                            |    O
                            |   -\-
                            |    |
                            |       
                            -
                    """,
              """
                            ------
                            |    |
                            |    O
                            |   -\-
                            |    
                            |    
                            -
                    """,
              """
                            ------
                            |    |
                            |    O
                            |   
                            |    
                            |   
                            -
                    """,
              """
                            ------
                            |    |
                            |    
                            |   
                            |    
                            |   
                            -
                    """,
              """
                    """
              ]
    return stages[tries]


the_game()
