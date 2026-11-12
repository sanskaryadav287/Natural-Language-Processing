re.search
## re.search() searches for a pattern anywhere in the string

import re
text =  "Python is easy! I love NLP."
result = re.search('Python',text)
if result:
    print('Result is found in text ')
else:
    print('result is not found in Text')





# re.findall()
# findall() returns all accurences of a patter.
import re 
text =  "I have 10 apples, 20 oranges, and 30 bananas."
result = re.findall(r'\d+',text)
print(result)




## without + of d
import re 
text = "I have 10 apples, 20 oranges, and 30 bananas."
result = re.findall(r'\d',text)
print(result)



# With search
import re 
text = "I have 10 apples, 20 oranges, and 30 bananas."
result = re.search(r'\d+',text)



# Extract all Email address
import re
text = '''
Ajay Bhati is employee our company and his email is : ajaynhati453@gmail.com
Arti sukla is employee our company and his email is : artisukla367@gmail.com
'''
result = re.findall(r'[a-zA-Z0-9._+%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',text)

print(result)

# eXTRACT pHONE nUMBER
text = 'I am the owner of this building my contact no is : 7906997240,8006191600'
phone_no = re.findall(r'\b\d{10}\b',text)
print(phone_no)




## Removing Punctuation
text = "Hello, World ! Python is amazing."
result = re.sub(r'[^\w\s]', '',text)
print(result)




# Removing Extra Space
text = '   Rajan  is  my childhood     friend  of class 2  nd.'
result = re.sub(r'\s+', ' ',text)

print(result)



# Extract Hastag
text = "I love #Python and #DataScience. #MachineLearning is interesting."
result = re.findall(r'#\w+',text)
print(result)




# Extract Mention
text = 'Thanks @rahul and @neha for attending the session.'
mention = re.findall(r'@\w+',text)
print(mention)



# Extract URL
text = """
 Visit https://www.python.org
or https://www.google.com for more information.
"""
url = re.findall(r'https:?//\S+',text)
print(url)





# Extract Words Starting with a specific letter
text = "Thanks @rahul and @neha for attending the session."
words = re.findall(r'\b[s]\w*',text)
print(words)





# Replce words using regex
text = 'Python is most powerful language. I teach python for students.'
new_text = re.sub(r'Python','Java',text)
print(new_text)



# Case senstive matching
text = "Python is easy. PYTHON is powerful.python is popular."
result = re.findall(r'Python',text,re.IGNORECASE)
print(result)




#Extract Dates
text = 'The NLP workshop is scheduled on 15-08-2024 at 10 AM.'
dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b',text)
print(dates)


text = 'Raja Ram is King of Ayodhya and He is lord of Hindnism.'
'Ayodhya' in text

import re
pattern = 'Ayodhya'
re.search(pattern,text)
match = re.search(pattern,text)
print(match)


import re
pattern = 'Not in text'
re.search(pattern,text)
match = re.search(pattern,text)
print(match)
print( match.span())
match.start()
match.end()
match = re.findall('Ayodhya',text)
print(match)
print(len(match))



for match in re.finditer('Ayodhya',text):
    print(match)



# Pattern ----------

import re 
text = 'You contact me on 488-6555-8945. '
phone = re.search(r'\d\d\d-\d\d\d\d-\d\d\d\d',text)
print(phone.group())




# Groups ---------
import re 
text = 'My contact no is 787-8547-9856.'
pattern = re.compile(r'\d{3}-\d{4}-\d{4}')
result = re.search(pattern,text)
print(result.group())
print(result.group(1))
print(result.group(2))
print(result.group(3))



## OR Operator    ---------
from Lemmatization_spaCy_NLTK import result
import re 
result = re.search('Ram|Raja','Ram is the God of Hindunism.')
print(result)



# The Wildcard Character  -----------
result = re.findall(r'..at','Cat on the Hat in a room.')
print(result)



result = re.findall(r'.at','Ram wear a hat and has a bat.')
print(result)

result = re.findall('..ng.','Amar singh is very reputed person.')
print(result)


result = re.findall('....ng.','Amar singh is very reputed person.')
print(result)


result = re.findall(r'\S+ed','Amar singh is very reputed person.')
print(result)


result = re.findall(r'\s+ed','Amar singh is very reputed person.')
print(result)











# Starts With and Ends With  ----------------
result = re.findall(r'\d$','100 is the sum of 2')
print(result)


result = re.findall(r'^\d','100 is the sum of 2')
print(result)




#   Exclusion  ---------------
text = ' There are 5 tables in 2 rooms and 1 home.'
result = re.findall(r'[^\d]',text)
print(result)


text = ' There are 5 tables in 2 rooms and 1 home.'
result = re.findall(r'[^\d]+',text)
print(result)



test_pharase= 'This is a string but it has punctuation. How can we remove it?'
result = re.findall(r'[^!.?]+',test_pharase)
print(result)

result = ''.join(re.findall(r'[^!.?]+',test_pharase))
print(result)



# Brackets for Grouping  ----------
text = "only find the hypen-words in this senntences. But you do not know how long-ish they are"
result = re.findall(r'[\w]+-[\w]+',text)
print(result)



# Perentheses for Multiple Options   ---------
#Find words that start with cat and end with one these options: 'fish', 'nap', or 'claw'

text = 'Hello, world you like some catfish?'
text2 = 'Hello, world you like to take a catnap'
text3 = 'Hello, have you seen this caterpillar'

result= re.search(r'cat(fish|nap|claw)',text)
print(result.group())


result= re.search(r'cat(fish|nap|claw)',text2)
print(result.group())


result= re.search(r'cat(fish|nap|claw)',text3)
print(result)