# Create a password checker
    # has to be at least 8 characters long
    # can contain letters, numbers or these symbols $%#@
    # ends with a number

# If we were to write this from scratch on regex101, it would look like this
    # 1) [A-Za-z0-9$%#@]{8,}\d
    # 2) Generate code and copy and paste to code here

import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = 'b@b.com'
pattern2 = re.compile(r"[A-Za-z0-9$%#@]{8,}\d")
password = 'passwordcheck$%#@99'

a = pattern.search(string)
check = pattern2.fullmatch(password)
print(check)        # password matched criteria