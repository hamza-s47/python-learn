phone_num = '311-246-3375'
text = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

def isPhoneChecked(num:str):
    if len(num) != 12:
        # print("Short or more numbers!")
        return False
    
    if  (not num[0:3].isdecimal()) or (not num[4:7].isdecimal() or  (not num[8:].isdecimal()) or (num[3] != '-') or (num[7] != '-')):
        # print("Invalid number")
        return False

    return True

# print(isPhoneChecked(phone_num))

for i in range(len(text)):
    if isPhoneChecked(text[i:i+12]):
        print(text[i:i+12])
