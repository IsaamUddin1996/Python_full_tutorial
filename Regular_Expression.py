import re
mystr = '''Manufacturing sector comprises of two sub-sectors viz. 
 Large Scale Manufacturing and Small Scale Manufacturing. 
 Large Scale manufacturing covers the establishments 432154-75839 
 registered under factories Act 1934 or qualifying for registration         allllllllll'''

patt = re.compile(r'covers')
# patt = re.compile(r'.') #for any character
# patt = re.compile(r'^Manufacturing') # ^ is use for (starts with)
# patt = re.compile(r'registration$') # $ is use for (ends with)
# patt = re.compile(r'al*') #ab yahan a ky sath jitne bhi l honge subb print hojaenge #for zero or 1
# patt = re.compile(r'al+') #ab yahan a ky sath jitne bhi l honge subb print hojaenge # atleast one l with a
# patt = re.compile(r'al{2}') # 2 a ky sath l jahan ho wohi print karo #exactly no of occurances
# patt = re.compile(r'(al){2}') #isse group banjaygea al ka 2 ka mtlb 2 group
#patt = re.compile(r'al{1}|an') #Either or or al print karega ya phir an

#Special Sequence

#patt = re.compile(r'\AManufacturing') #q k Manufacturing se start ho rha hai

# patt = re.compile(r'\bAct')
# patt = re.compile(r'ing\b') # \b baad my lagane ka mtlb hai ky jo ing pr ending ho rhi hai wo print krdo
# patt = re.compile(r'\d{3}-\d{4}')
matches = patt.finditer(mystr)
for match in matches:
    print(match)
    # print(mystr[142:148])


'''    
Meta Characters
[] A set of characters
\ Signals a special sequence (can also be used to escape special characters)
. Any character (except newline character)
^ Starts with
$ Ends with
* Zero or more occurrences
+ One or more occurrences
{} Exactly the specified number of occurrences
| Either or
() Capture and group
Special Sequences
\A Returns a match if the specified characters are at the beginning of the string
\b Returns a match where the specified characters are at the beginning or at the end of a word r"ain\b"
\B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word


\d Returns a match where the string contains digits (numbers from 0-9)
\D Returns a match where the string DOES NOT contain digits
\s Returns a match where the string contains a white space character
\S Returns a match where the string DOES NOT contain a white space character
\w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
\W Returns a match where the string DOES NOT contain any word characters
\Z Returns a match if the specified characters are at the end of the string '''