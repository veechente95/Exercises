# build a simple counter that counts items in list

# loop over this iterable list to sum up total of list
my_list = [1,2,3,4,5,6,7,8,9,10]

counter = 0
for item in my_list:
    counter = counter + item    # indentation is sign of looping

print(counter)