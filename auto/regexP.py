import pyperclip, re

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ # username
    @ # @ symbol
    [a-zA-Z0-9.-]+ # domain name
    (\.[a-zA-Z]{2,4}) # dot-something
)''', re.VERBOSE)

pyperclip.copy('My name is Hamza')
x = pyperclip.paste()
print(x)