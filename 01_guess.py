import random


def intro():
    print('Welcome to Guess Me!\n')
    print('Try to guess the number from 1 to 100')
    print("If your 1st guess is within 10 of the number I'd say 'WARM!'")
    print("further than 10 away from the number I'd say 'COLD!'")
    print('Every next turn I will provide tips if you are getting closer to \
        \nthe correct number.\n')
    print("Let\'s Play!\n")


def game():
    var1 = random.randint(1, 101)
    guesses = [0]
    while True:
        guess = int(input('- I\'m thinking of a number between 1 and 100.\n \
            \nWhat\'s your guess?'))
        if guess < 1 or guess > 100:
            print('OUT OF BOUNDS! Please try again: ')
            continue
        if guess == var1:
            print('Congrats!')
            print()
            print(f'Number of Guesses: {len(guesses)}')
            break
        guesses.append(guess)
        if guesses[-2]:
            if abs(var1 - guess) < abs(var1 - (guesses[-2])):
                print("Warmer!")
            else:
                print("Colder!")
        else:
            if abs(var1 - guess) < 10:
                print('Warm!')
            else:
                print('Cold!')


def restart():
    yeslist = ['yes', 'y', 'ye']
    restart = input("\nInput 'Y' if you want to play again, 'X' to  exit) > ")
    if restart.lower() in yeslist:
        import os
        os.system('cls')
        main()
    else:
        exit()


def main():
    intro()
    game()
    restart()


if __name__ == '__main__':
    main()
