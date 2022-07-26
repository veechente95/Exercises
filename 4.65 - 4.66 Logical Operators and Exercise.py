# Logical Operators: and, or, not >, < , >=, <=, ==, !=

# Exercise
is_magician = False
is_expert = True

# Check if magician AND expert are true, then print "You are a master magician"
# Check if magician but not expert: "At least you're getting there"
# if you are not a magician: "You need magic powers"

if is_magician and is_expert:
    print("You are a master magician")
elif is_magician and not is_expert:
    print("At least you're getting there")
elif not is_magician:
    print("You need magic powers")
