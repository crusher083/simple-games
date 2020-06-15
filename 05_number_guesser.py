import os


def intro():
    print('Hi!')
    print('Choose any number form 0 to 100 and I will try to guess it!')
    input('\nWhen ready press Enter')


def guess():
    l = 0
    h = 100
    m = 50
    counter = 0
    cond = input (f'Is your number {m}?\n0 - too low\n1 - correct\n2 - too high\n')
    while cond != '1':
        counter += 1
        if cond == '0':
            l = m + 1
        elif cond == '2':
            h = m - 1
        m = (l + h) / 2
        cond = input(f'Is your number {int(m)}?\n0 - too low\n1 - correct\n2 - too high\n')
    print('Got it!')
    if counter < 3:
        print(f'Only {counter} tries! Damn, I\'m good!')
    elif 3 <= counter <= 10:
        print(f'{counter} tries, not bad for a robot')
    elif counter > 10:
        print(f'{counter} tries. Better luck next time!')


def replay():
    yeslist = ['yes', 'ye', 'y']
    nolist = ['no', 'n']
    choice1 = input('Wanna play again? Y or N\n')
    if choice1.lower() in yeslist:
        os.system('cls')
        game()
    elif choice1.lower() in nolist:
        quit()
    else:
        print('Incorrect input!')
        replay()


def game():
    intro()
    guess()
    replay()


if __name__ == '__main__':
    game()
