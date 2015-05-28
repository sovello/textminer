import re

def phone_number(text):
    match = re.findall(r'(\d{3})\D*(\d{3})\D*(\d{4})', text)
    if not match:
        return None
    else:
        code = match[0]
        number = "{}-{}".format(code[1], code[2])
        dic = {"area_code":code[0], "number":number}
        return dic

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

def date(text):
    sep_l = r'(\d{1,2})/(\d{1,2})/(\d{2,4})'
    sep_d = r'(\d{2,4})\-(\d{2})\-(\d{2})'
    if re.search('-', text):
        match = re.search(sep_d, text)
        if match == None:
            return False
        else:
            return True
    elif re.search('/', text):
        match = re.search(sep_l, text)
        if match == None:
            return False
        else:
            True
    else:
        return False

def hdate(date):
    monts = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
    if re.search(r'/', date):
        dt = date.split('/')
        if int(dt[0]) == 2:
            if int(dt[2]) % 4 == 0  and int(dt[1]) > 29:
                return False
            elif int(dt[2]) % 4 != 0  and int(dt[1]) > 28:
                return False
            else:
                return date_format(int(dt[0]), int(dt[1]),int(dt[2]))
        else:
             if int(dt[0]) in [4,6,9,11] and int(dt[1]) > 30:
                 return False;
             elif int(dt[0]) in [1,3,5,7,8,10,12] and int(dt[1]) > 31:

                 return False
             else:
                 return True
    else:
        if re.match(r'^\d+', date):
            match = date.split(' ')
            year = int(match[0])
            day = int(match[2])
            month = match[1][0:3].lower()
            month = monts.index(month[0:3])+1
            return True
        elif re.match(r'^[a-zA-Z]', date):
            match = re.sub(r'([\.,])', '', date)
            match = match.split(' ')
            year = int(match[2])
            day = int(match[1])
            month = match[0]
            month = month[0:3].lower()
            month = monts.index(month[0:3])+1
            return True

def address(text):
    if not re.search(r'^\d', text):
        return False
    else:
        addresse = r'(^\d{3,}\s+\w+(?:\s+\w+))(?:[,?\n?])'
        state = r'(\b[A-Z]{2}\b)'
        zcode = r'(\d{5}\-?\d{0,4})'
        city1 = r'(?:\n?|,?)\s*(\w+\s*)(\w+\s*)(?:, \b[A-Z]{2}\b)'
        city2 = r'(?:\n?|,?)\s*(\w+\s*\w+\s*)(?:, \b[A-Z]{2}\b)'
        city = r'(?:\n+|,+){1}\s*([\w+\.?_?\d?\-?\s*]+)(?:, \b[A-Z]{2}\b)'

        city = re.search(city, text).groups()
        addresse = re.search(addresse, text).groups()
        state = re.search(state, text).groups()
        zcode = re.search(zcode, text).groups()
        code= zipcode(zcode[0])
        if city or addresse or state or zcode or code:
            return True
        else:
            return False
