import math
import re

def words(text):
    match = re.findall(r'\d*\-?[a-zA-Z\-]+', text, re.IGNORECASE)
    return match if len(match) > 0 else None

def phone_number(text):
    match = re.findall(r'(\d{3})\D*(\d{3})\D*(\d{4})', text)
    if not match:
        return None
    else:
        code = match[0]
        number = "{}-{}".format(code[1], code[2])
        dic = {"area_code":code[0], "number":number}
        return dic


def money(text):
    if not re.match(r'^\$(\d+)', text):
        return None
    else:
        match = re.findall('(\$\d+)(,*\d{3})*(\.[\d]{2})?$', text)
        print(match)

print(money('$12'))
print(re.match(r'(,\d{2}\b)', '$12,34'))

# helper

def round(number):
    return math.round(float(number), 2)

def zipcode(text):
    if not re.search(r'-', text) and len(text) == 5:
        return {"zip":text, "plus4": None}
    elif re.search(r'-', text):
        match = re.search(r'(\d{5})\-?(\d{4})?', text)
        if match == None:
            return None
        else:
            zipp, plus4 = match.groups()
            if plus4 == None or zipp == None:
                return None
            else:
                return {"zip":zipp, "plus4":plus4}
    else:
        return None

def date(text):
    sep_l = r'(\d{1,2})/(\d{1,2})/(\d{2,4})'
    sep_d = r'(\d{2,4})\-(\d{2})\-(\d{2})'
    if re.search('-', text):
        match = re.search(sep_d, text)
        if match == None:
            return None
        else:
            year, month, day = match.groups()
            return date_format(month, day, year)
    elif re.search('/', text):
        match = re.search(sep_l, text)
        if match == None:
            return None
        else:
            month, day, year = match.groups()
            return date_format(month, day, year)
    else:
        return None

###DRY###
def date_format(month, day, year):
    return {"month":int(month), "day":int(day), "year":int(year)}

def hdate(date):
    monts = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
    if re.search(r'/', date):
        dt = date.split('/')
        print(date+" separated by /")
        if int(dt[0]) == 2:
            if int(dt[2]) % 4 == 0  and int(dt[1]) > 29:
                return None
            elif int(dt[2]) % 4 != 0  and int(dt[1]) > 28:
                return None
            else:
                return date_format(int(dt[0]), int(dt[1]),int(dt[2]))
        else:
             if int(dt[0]) in [4,6,9,11] and int(dt[1]) > 30:
                 return None;
             elif int(dt[0]) in [1,3,5,7,8,10,12] and int(dt[1]) > 31:

                 return None
             else:
                 return date_format(int(dt[0]), int(dt[1]), int([dt2]))
    else:
        if re.match(r'^\d+', date):
            match = date.split(' ')
            year = int(match[0])
            day = int(match[2])
            month = match[1][0:3].lower()
            month = monts.index(month[0:3])+1
            return date_format(month, day, year)
        elif re.match(r'^[a-zA-Z]', date):
            match = re.sub(r'([\.,])', '', date)
            match = match.split(' ')
            year = int(match[2])
            day = int(match[1])
            month = match[0]
            month = month[0:3].lower()
            month = monts.index(month[0:3])+1
            return date_format(month, day, year)


def email(text):
    match = re.findall(r'\b([a-zA-Z_]+[\d{0,}\.?\-?]*[a-zA-Z]*)@([a-zA-Z]*\.\w{2,3})\b', text)
    if len(match) == 0:
        return None
    else:
        match = match[0]
        return {"local":match[0], "domain":match[1]}

def address(text):
    if not re.search(r'^\d', text):
        return None
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
 #       print(code)
        return {"address":addresse[0], "city":city[0], "state":state[0], "zip":code['zip'], "plus4":code['plus4']}
        #return re.search(zcode,text)
