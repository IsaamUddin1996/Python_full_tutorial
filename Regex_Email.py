# \B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word

import re

str = '''Manufacturing sector comprises of two sub-sectors viz. 
 Large Scale Manufacturing Azzam@Hotmail.com and Small Scale Manufacturing. 
 Large Scale manufacturing covers the ism@yahoo.com establishments 432154-75839 
 registered under Saif@gm%ail.com factories Act 1934 or qualifying for registration '''

mystr = re.compile(r'\S+@\S+')

matches = mystr.finditer(str)
with open("Regularfile","w") as f:
    for matchabc in matches:
        print(matchabc.group())
        f.write(f"email: " + matchabc.group().capitalize() + "\n")

# abc = re.findall('\S+@\S+', str)
# print(abc)
