# Exercise 1 - create a one line lambda expression that is going to square our list

my_list = [5,4,3]
print(list(map(lambda item: item ** 2, my_list)))



# Exercise 2 - Sort based on the second value from lowest to highest (-1, 2, 3, 9)

a = [(0,2), (4,3), (10,-1), (9,9)]
a.sort(key = lambda x: x[1])
print(a)