import re

# Matching number pattern
regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = regex.search('My number is 415-555-1011.')
country_code, main_num = mo.groups()
# print(country_code, main_num)
# print(mo.group())
# print(mo.group(1), mo.group(2))

# Matching String Pattern
str_regex = re.compile(r'Hamza|Sidd')
reg_search = str_regex.search('My name is Hamza but you can call me Sidd')
# print(reg_search.group())
str_regex2 = re.compile(r'Hamza( Siddiqui| Faheem)')
reg_search2 = str_regex2.search('My name is Hamza Faheem')
# print(reg_search2.group())