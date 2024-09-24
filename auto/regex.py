import re

# MATCHING NUMBER PATTERN (01)
regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = regex.search('My number is 415-555-1011.')
all = regex.findall('My number is 415-555-1011. I have another number which is: 311-123-9966')
country_code, main_num = mo.groups()
# print(country_code, main_num)
# print(mo.group())
# print(mo.group(1), mo.group(2))
# print(all)

# MATCHING STRING PATTERN (02)
str_regex = re.compile(r'Hamza|Sidd')
str_regex2 = re.compile(r'Hamza( Siddiqui| Faheem)')
str_regexOptional = re.compile(r'(M.)?Hamza Siddiqui')
str_regexAsteric = re.compile(r'(M.)*Hamza Siddiqui')
str_regexPlus = re.compile(r'(M.)+Hamza Siddiqui')  #it should has one (M.)

reg_search = str_regexPlus.search('My name is M.M.M.Hamza Siddiqui but you can call me Sidd')
# print(reg_search.group())

# GREEDY AND NON-GREEDY MATCHING (03)
greedy_regex = re.compile(r'(Ha){3,5}')
non_greedy_regex = re.compile(r'(Ha){3,5}?')

gr_search = non_greedy_regex.search('HaHaHaHaHaHa')
# print(gr_search.group())

# CHARACTER CLASSES
c_regex = re.compile(r'[AEIOU]', re.I) # Case insensitive
t_regex = re.compile(r'\W')
x = t_regex.findall('text')
print(x)
