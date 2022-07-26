# Code so sort out duplicates in list
some_list = ['a', 'b', 'c', 'b','d', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)       # ['b', 'n']

# Exercise - Make this list neater using comprehensions
duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))
print(duplicates)       # ['b', 'n']
