print("Hello, welcome to Tic Tac Toe. Enjoy the game!")

# constructed board layout from top to bottom starting with 1
board = {'1': ' ', '2': ' ', '3': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '7': ' ', '8': ' ', '9': ' '}

keys = []

for key in board:
    keys.append(key)


def layout(board):
    print(board['1'] + '/' + board['2'] + '/' + board['3'])
    print('-+-+-')
    print(board['4'] + '/' + board['5'] + '/' + board['6'])
    print('-+-+-')
    print(board['7'] + '/' + board['8'] + '/' + board['9'])
    print('-+-+-')


# defining player turns
def game():
    turn = "X"
    count = 0

    for i in range(10):
        layout(board)
        print(" (Board is listed from 1-9 in order left to right). ")
        print(" It is now the turn of " + turn + " which spot will you choose?  ")

        move = input()

        if board[move] == ' ':
            board[move] = turn
            count += 1
        else:
            print(" Sorry this spot has been filled, please choose another place. ")
            continue
        # loop for game

        if count >= 5:
            if board['7'] == board['8'] == board['9'] != ' ':
                layout(board)
                print(" \nGame Over\n ")
                print("Player " + turn + " won!! ")

                break

            if board['4'] == board['5'] == board['6'] != ' ':
                layout(board)
                print(" \nGame Over\n ")
                print("Player " + turn + " won!! ")

                break

            if board['1'] == board['2'] == board['3'] != ' ':
                layout(board)
                print(" \nGame Over\n ")
                print("Player " + turn + " won!! ")

                break

            if board['1'] == board['4'] == board['7'] != ' ':
                layout(board)
                print(" \nGame Over\n ")
                print("Player " + turn + " won!! ")

                break

            if board['2'] == board['5'] == board['8'] != ' ':
                layout(board)
                print(" \nGame Over\n ")
                print("Player " + turn + " won!! ")

                break

            if board['3'] == board['6'] == board['9'] != ' ':
                layout(board)
                print(" \nGame Over\n ")
                print("Player " + turn + " won!! ")

                break

            if board['1'] == board['5'] == board['9'] != ' ':
                layout(board)
                print(" \nGame Over\n ")
                print("Player " + turn + " won!! ")

                break

            if board['3'] == board['5'] == board['7'] != ' ':
                layout(board)
                print(" \nGame Over\n ")
                print("Player " + turn + " won!! ")

                break

        # restart game
        if count == 9:
            print("\nGame Over\n")
            print("This is a tie! ")

        if turn == "X":
            turn = "O"
        else:
            turn = "X"

    restart = input(" Do you want to play again? Y or N? ").lower()

    if restart == 'y':
        for key in keys:
            board[key] = ' '


game()
