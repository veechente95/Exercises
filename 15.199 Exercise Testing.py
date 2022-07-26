# unittest test's each piece of unit in code
# Break this down into smaller functions using unittest
# Look at video for breakdown again.
    # Essentially more testing means better and cleaner code
    # depending on job you might need to focus more on writing or testing code


import random

answer = random.randint(1, 10)
while True:
    try:
        guess = int(input('guess a number between 1 through 10:'))
        if 0 < guess < 11:         # same as --- if int(guess) > 0 and int(guess) < 11:
            if (guess) == answer:
                print('You fucking guessed it! What a genius!')
                break
        else:
            print('hey dumbass, I said between 1 and 10')
    except ValueError:
        print('please enter a number')
        continue
