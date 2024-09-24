import pyperclip, re

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ # username
    @ # @ symbol
    [a-zA-Z0-9.-]+ # domain name
    (\.[a-zA-Z]{2,4}) # dot-something
)''', re.VERBOSE)

# x = emailRegex.findall('')
# print(x)
emails= "In the bustling world of technology, many individuals are making their mark. For instance, you might find James Smith at james.smith123@example.com, while his colleague, Sarah Johnson, can be reached at sarah.johnson456@domain.com. Over in marketing, Mike Brown shares insights through mike.brown789@webmail.com, and Lisa White connects with clients at lisa.white2023@mailservice.org. Meanwhile, in the development team, you’ll often see Alex Green emailing updates from alex.green.dev@programming.com and Jessica Blue, who frequently collaborates with partners via jessica.blue@partnershub.net. Don't forget about Emily Clark, who shares her innovative ideas at emily.clark@creativeworks.com, or Robert Taylor, who updates everyone at robert.taylor@businessmail.com. Last but not least, you can also contact David Harris at david.harris2024@startupmail.com and Karen Lewis at karen.lewis@techgroup.org for more insights."

matches = []

for groups in emailRegex.findall(emails):
    matches.append(groups[0])

print(matches)