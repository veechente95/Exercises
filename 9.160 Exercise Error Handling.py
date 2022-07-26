# Error Handling Exercise

while True:
    try:
        age = int(input('what is your age?'))
        10/age
    except ValueError:                      # if there is a ValueError, try this
        print('please enter a number')
    except ZeroDivisionError:               # if there is a ZeroDivision Error, try this
        print('please enter an age higher than 0')
    else:                                   # if there is no error, do this
        print('thank you!')
        break                               # prevents from looping
    finally:                                # will always run at the end once everything is executed
        print('ok, I am finally done')


