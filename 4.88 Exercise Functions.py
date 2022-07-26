# create a function called highest_even that's going to pull the highest even number from a list

# First create a list of the even numbers since we don't care about odd
def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)           # python has a max function to get max value

print(highest_even([10,2,3,4,8,11]))