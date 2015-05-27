import re

def words(text):
    match = re.findall(r'\d*\-?[a-zA-Z\-]+', text, re.IGNORECASE)
    return match if len(match) > 0 else None
print(words('12'))
