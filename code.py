import time
import random

name = input('What`s your name?')
print(f'Hello, {name}!')

time.sleep(1)

question = input('Wanna play?(yes/no)')
if question == 'yes':
    print('OK, let`s play!')
else:
    print('OK, Bye!')
    quit()


print('Start guessing...')
time.sleep(0.5)

words = ["sunday", "secret", "hangman", "thunder", "python"]
secret_word = random.choice(words)


def get_guess():

    dashes = "-" * len(secret_word)
    guesses_left = 10

    while guesses_left > -1 and not dashes == secret_word:

        print(dashes)
        print(str(guesses_left))

        my_guess = input("Guess:")

        if len(my_guess) != 1:
            print("Write only one letter!")

        elif my_guess in secret_word:
            print("That letter is in the secret word!")
            dashes = update_dashes(secret_word, dashes, my_guess)

        else:
            print("That letter is not in the secret word!")
            guesses_left -= 1

    if guesses_left < 0:
        print("You lose. The word was: " + str(secret_word))
    else:
        print("Congrats! You win. The word was: " + str(secret_word))


def update_dashes(secret, cur_dash, rec_guess):
    result = ""

    for i in range(len(secret)):
        if secret[i] == rec_guess:
            result = result + rec_guess

        else:
            result = result + cur_dash[i]

    return result


get_guess()
