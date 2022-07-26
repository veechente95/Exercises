
# Exercise -  Building a translator that translates a file to Japanese

#1) Install the package you found on Google and use as python module

from translate import Translator

translator = Translator(to_lang="ja")
try:
    with open('sad.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('sad-japanese.txt', mode='w') as my_file2:      # # Let's finalize this by converting the doc to a translated version
            my_file2.write(translation)
except FileNotFoundError as e:
    print('check your file path silly!')
