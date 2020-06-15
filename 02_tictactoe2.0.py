import os


def enter_name(player):
    print(f'{player} Enter your name, please:')
    player = input()
    player = f'>{player}<'
    print(f'Welcome {player}!')
    return player


def x_or_o(player1, player2):
    print(f'{player1} Do you want to be X or O?')
    while True:
        inp1 = input("")
        if inp1.upper() == 'X':
            print(f'{player1} starts the game!')
            break
        elif inp1.upper() == 'O':
            print(f'{player2} starts the game!')
            player1, player2 = player2, player1
            break
        else:
            print('Please choose X or O!')
    return player1, player2


def board_example():
    print('Numbers represent the position of X or O\
 and reflect NumPad on keyboard')
    print(f'{7:^3} | {8:^3} | {9:^3}\n{4:^3} | {5:^3} |\
 {6:^3}\n{1:^3} | {2:^3} | {3:^3}\n')


def board_call(board):
    print(f"""{board[2][0]:^3} | {board[2][1]:^3} | {board[2][2]:^3}
{board[1][0]:^3} | {board[1][1]:^3} | {board[1][2]:^3}
{board[0][0]:^3} | {board[0][1]:^3} | {board[0][2]:^3}""")


def check_input(turn):
    while True:
        if turn % 2 == 0:
            num = input(f'{player2}, please choose field from 1 to 9\n')
        else:
            num = input(f'{player1}, please choose field from 1 to 9\n')
        if num.isdigit() and 9 >= int(num) >= 1:
            break
        else:
            print('Incorrect input!')
    return num


def check_if_empty_replace(num, turn, board):
    x = ((int(num) - 1) // 3)
    y = (int(num) - 1) % 3
    if board[x][y] == 'O' or board[x][y] == 'X':
        print(f'The field {num} is already taken!')
    else:
        if turn % 2 == 0:
            board[x][y] = 'O'
        else:
            board[x][y] = 'X'
    return board


def rows_159(board):
    yield from board
    yield [board[i][i] for i in range(len(board))]


def all_lines(board):
    yield from rows_159(board)
    yield from rows_159(list(zip(*reversed(board))))


def win(board):
    for line in all_lines(board):
        if len(set(line)) == 1 and line[0] != '-':
            return line[0]
    return None


def replay():
    yeslist = ['yes', 'ye', 'y']
    nolist = ['no', 'n']
    choice1 = input('Wanna play again? Y or N\n')
    if choice1.lower() in yeslist:
        while True:
            choice2 = input('Change names? Y or N\n')
            if choice2.lower() in yeslist:
                os.system('cls')
                enter_name()
                game(player1, player2)
                break
            elif choice2.lower() in nolist:
                os.system('cls')
                game(player1, player2)
                break
            else:
                print('Incorrect input!')
    elif choice1.lower() in nolist:
        quit()
    else:
        print('Incorrect input!')
        replay()


def game(player1, player2):
    player1, player2 = x_or_o(player1, player2)
    board_example()
    board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    turn = 1
    playing = True
    while playing and turn <= 9:
        num = check_input(turn)
        check_if_empty_replace(num, turn, board)
        board_call(board)
        if win(board) == 'X':
            print(f'{player1} wins!')
            playing = False
        elif win(board) == 'X':
            print(f'{player2} wins!')
            playing = False
        turn += 1
        if turn == 10:
            print("It's a tie!")
            playing = False
    replay()


def main():
    print("Welcome to Tic Tac Toe Game!\n")
    print('Grab your friend!')
    print("And let's play!\n")
    player1 = '>Player1<'
    player2 = '>Player2<'
    player1 = enter_name(player1)
    player2 = enter_name(player2)
    game(player1, player2)


if __name__ == "__main__":
    main()
