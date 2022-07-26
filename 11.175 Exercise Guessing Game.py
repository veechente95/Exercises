# run a game program asking the user to guess a number between 1 and 10
# have program run until user guesses it right

# 1) generate a number 1~10
from random import randint
import sys
answer = randint(1, 10)

while True:
    try:
        guess = input('guess a number between 1 through 10:')
        if 0 < int(guess) < 11:         # same as --- if int(guess) > 0 and int(guess) < 11:
            if int(guess) == answer:
                print('You fucking guessed it! What a genius!')
                break
        else:
            print('hey dumbass, I said between 1 and 10')
    except ValueError:
        print('please enter a number')
        continue
