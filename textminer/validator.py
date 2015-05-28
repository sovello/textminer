import re

'''
def phone_number(text):
    match = re.findall(r'\(?(\d{3})\)?\-*\s*\.*(\d{3})\-*\.*\s*(\d{4})', text)
    print(match)
    if len(match) < 3:
        return False
    else:
        return True
'''

def phone_number(text):
    match = re.findall(r'\(?(\d{3})\)?\-*\s*\.*(\d{3})\-*\.*\s*(\d{4})', text)
    if len(match) < 3:
        return None
    else:
        code = match[0]
        number = "{}-{}".format(match[1], match[2])
        dic = {"area_code":code, "number":number}
        return dic
print(phone_number('919-555-1212'))


#print(phone_numbers('555-1212'))

def binary(number):
    return re.match(r'\A[01]+', number)

def binary_even(number):
    return re.match(r'\A[01]+0\Z', number)

def hex(number):
    return re.match(r'\b[0-9A-Fa-f]+\b', word)

def word(text):
    match = re.findall(r'\d*\-?[a-zA-Z0-9\-]+', text, re.IGNORECASE)
    return True if len(match) > 0 else False

def words(text, count=1):
    if word(text):
        if len(text.split()) == count:
            return True
        else:
            return False
    else:
        return False
