
# Create a super list using the class SuperList():
# add code that allows us to use it like a list
# superlist is going to have a dunder method __len__ that we are going to modify and have it return 1000

# how are we going to use the power a list already has and modify __len__ dunder?

# class SuperList():
#     def __len__(self):
#     pass
#
# super_list1 =SuperList():
#
# len(super_list1)
# super_list1.append(5)
# super_list1[5]

class SuperList(list):
    def __len__(self):
        return 1000

super_list1 = SuperList();

print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
print(issubclass(SuperList, list))  # a way to check