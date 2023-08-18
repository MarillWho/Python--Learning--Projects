import pygame
import random
import os

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Guess the Number')
font = pygame.font.Font(pygame.font.get_default_font(), 36)


def draw():
    screen.fill((255, 255, 255))
    text = font.render('Hello World', False, pygame.Color('red'), pygame.Color('blue'))
    rect = text.get_rect()
    center = (300, 300)
    textRect.center = center
    screen.blit(text, textRect)
    pygame.display.update()
    main()


def main():
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


from random import randint


def game():
    while True:
        first = 0
        last = 50
        tries = 4
        number = randint(first, last)
        print(" The computer chose a number between", first, "and", last)
        guess = None

        while guess != number and tries > 0:
            print(" You have", tries, "tries!")
            text = input("Please guess the number/integer: ")
            guess = int(text)

            if guess < number:
                tries = tries - 1
                print(" The number/integer is higher. ")
            elif guess > number:
                tries = tries - 1
                print(" The number/integer is lower. ")

            elif guess == number:
                print(" Yay!! You got it right!!")

            if tries == 0:
                print(" Oh no!! There are no more tries.")

        # play again function
        user = input("Would you like to play another round? Y or N? ").lower()
        if not user:
            break
        else:
            continue


if __name__ == '__main__':
    main()

# dev notes:
# how to input error message for non integers
