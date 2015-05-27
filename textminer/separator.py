import math
import re

def words(text):
    match = re.findall(r'\d*\-?[a-zA-Z\-]+', text, re.IGNORECASE)
    return match if len(match) > 0 else None

def phone_numbers(text):
    match = re.findall(r'\(?(\d{3})\)?\-*\s*\.*(\d{3})\-*\.*\s*(\d{4})', text)
    if len(match) < 3:
        return None
    else:
        code = match[0]
        number = "{}-{}".format(match[1], match[2])
        dic = {"area_code":code, "number":number}
        return dic
        #string = 'area_code":"{}", "number":"{}-{}"'.format(*match.groups())
        #return string

#print(phone_numbers('555-1212'))

def money(text):
    match = re.search(r'^(${1})(\d+,\d+{3}\.?\d*)', text)
    cur = match[0]
    amount = match[1]

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
    pass

def email(text):
    match = re.findall(r'\b([a-zA-Z_]+[\d{0,}\.?\-?]*[a-zA-Z]*)@([a-zA-Z]*\.\w{2,3})\b', text)
    if len(match) == 0:
        return None
    else:
        match = match[0]
        return {"local":match[0], "domain":match[1]}
        #return match

def address(text):
    match = re.search(r'', text)
        #print(email('viio_lakuku6@gmail.com'))
