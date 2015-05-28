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

#print(phone_number('919 555-1212'))

def money(text):
    #'\$\d+(,[\d]{3})*(\.[\d]{2})?$'
    match = re.findall(r'(\$\d+)((?:,)?[\d]{3})*\.([\d]{2})?', text)
    print(match)
    #cur = match[0]
    #amount = match[1]

money("$45,555,555.55")
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

txt = ("""368 Agness Harbor
     Port Mariah_scholes123, MS 63293""")
t = "8264 Schamberger Spring, matem.bwe njom-be Jordanside, MT 98833-0997"
z="Lake Joellville, NH"
#sth = address(t)
#print(sth)

