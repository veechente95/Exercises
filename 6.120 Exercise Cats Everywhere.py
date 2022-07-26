#Given the below class:
# 1 Instantiate the Cat object with 3 cats

class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 2 Create a function that finds the oldest cat
pet1 = Cat('Tom', 62)
pet2 = Cat('Jerry', 58)
pet3 = Cat('Miracle', 100)

def oldest_cat(*args):
    return max(args)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest ccat is {oldest_cat(pet1.age, pet2.age, pet3.age)} years old')