# Exercise - Check for duplicates and print what the duplicate values are

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

ducplicates = []                        # a variable that we are going to populate with duplicate values
for value in some_list:
    if some_list.count(value) > 1:
        ducplicates.append(value)

print(ducplicates)                      # Gives you ['b', 'b', 'n', 'n'] which has multiple. We only need one


# This is how we would prevent doubles from showing
ducplicates = []     # a variable that we are going to populate with duplicate values
for value in some_list:
    if some_list.count(value) > 1:
        if value not in ducplicates:
            ducplicates.append(value)

print(ducplicates)
