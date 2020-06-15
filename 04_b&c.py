import random
print('Welcome to Bulls&Cows!\n')
print('Bulls are digits that are right and in place.')
print('Cows are digits that are right, but in wrong place.')
print('For every number in the wrong place, you get a cow.\
       \nFor every one in the right place, you get a bull')


def check_input_num():
    num = input('How long the number should be?\n')
    while True:
        if num.isdigit() and int(num) <= 15 and int(num) >= 1:
            break
        else:
            print('Incorrect input!')
    return num


def move(rnd, n, guesses):
    counter_b = 0
    counter_c = 0
    while True:
        guess = input('Please, enter your guess:\n')
        if guess.isdigit():
            if len(guess) == int(n):
                break
            elif len(guess) > int(n):
                print('Guess is too long!')
            elif len(guess) < int(n):
                print('Guess is too short!')
        else:
            print('Incorrect input!')
    if guess == rnd:
        print(f'Correct! The right answer is {rnd}')
        print(f'Your number of guesses: {guesses}')
        playing = False
    else:
        for i in range(len(rnd)):
            if guess[i] == rnd[i]:
                counter_b += 1
            elif guess[i] in rnd:
                counter_c += 1
        print(f'Your guess contains {counter_b} Bulls & {counter_c} Cows')
        playing = True
    guesses += 1
    return playing, guesses


def game():
    n = check_input_num()
    rnd = str(random.randint(10**(int(n) - 1), (10**int(n)) - 1))
    playing = True
    guesses = 0
    while playing:
        playing, guesses = move(rnd, n, guesses)


def replay():
    replay = input("Would you like to play another hand? Enter 'Y' or 'N':\n ")
    if replay[0].lower() == 'y':
        game()
    else:
        print("Thanks for playing!")


def main():
    game()
    replay()


if __name__ == '__main__':
    main()
