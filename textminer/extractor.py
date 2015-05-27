import re
#class extractor(object):

def phone_numbers(text):
    return re.findall(r'\(?\d{3}\)?[\s|\-]\d{3}[\s|\-]\d{4}', text)


def emails(text):
    return re.findall(r'\b[a-zA-Z]+[\d*_?\.?\-?]?[a-zA-Z]*@[a-zA-Z]*\.\w{2,3}\b', text)

    
if __name__ == '__main__':
    ex = extractor()
    ex.phone_numbers('at (454) 999-1212 You can contact me at (919) 123-4569 at your convenience.')
    txt = '''Veggies es bonus vobis, proinde vos postulo essum magis kohlrabi
    welsh onion daikon amaranth@gmail.com tatsoi tomatillo azuki bean garlic.

    Gumbo beet greens corn soko endive gumbo gourd. Parsley shallot courgette
    tatsoi pea@sprouts.org fava bean collard greens dandelion okra wakame
    tomato. Dandelion cucumber.earthnut@pea.net peanut soko.zucchini.'''
    ex.emails(txt)
