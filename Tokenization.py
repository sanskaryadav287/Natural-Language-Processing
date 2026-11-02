
## 1. Word Tokenize

# import nltk
# # pyrefly: ignore[missing-import]
# from nltk.tokenize import word_tokenize

# text = "My name is Sanskar and I am a student."
# token = word_tokenize(text)
# print(token)


# ## 2. Sentence Tokenize 
# from nltk.tokenize import sent_tokenize

# text = '''Hello, How are you ? 
# I am fine and I am from India. I hope you are also fine.'''

# sentence = sent_tokenize(text)
# print(sentence)


# ## 3. Tokenizing  Userinput 
# from nltk import sent_tokenize
# from pydantic._internal import _schema_generation_shared
# text = input('enter some text:-')

# sentence= sent_tokenize(text)
# print(sentence)


# ## 5: tokenization with Punctuation
# text = "Hello, How are you ? I an fine!."
# from nltk.tokenize import word_tokenize
# token = word_tokenize(text)
# print(token)



# ## 6: Tokenization with numbers 
# from nltk import word_tokenize
# text = 'This is famous sweet and his price is 15875 per 1 kg.'
# tokens = word_tokenize(text)
# print(tokens)


# ## 7: Tokenization with Contraction
# from nltk import word_tokenize
# text = "I won't, won't's you, won't you do that?"
# tokens = word_tokenize(text)
# print(tokens)


# ## 8:Sentences Tokenize + word Tokenize
# from nltk import word_tokenize
# from nltk import sent_tokenize
# text =  """ Python is easy to learn.
# NLTK provides many NLP tools.
# Tokenization is an important NLP tasks. """

# sentences = sent_tokenize(text)
# for sentence in sentences:
#     word = word_tokenize(sentence)
#     print(word)



# ## 9: Count Number of tokens
# from nltk import word_tokenize
# text = "Python is easy to learn. NLTK provides many NLP tools."
# tokens = word_tokenize(text)
# print('Tokens:',tokens)
# print(len(tokens))



# ## 10: Count Number of Letters

# text = "Python is most powerful language."

# letters = [char for char in text if char.isalpha()]

# print("Letters:", letters)
# print("Number of Letters:", len(letters))



# ## 11:Count only words
# from nltk import word_tokenize
# import string 

# text = "Hello! Sanskar, how are you ?"
# tokens  = word_tokenize(text)
# words = [token for token in tokens if token not in string.punctuation]
# print(words)
# print(len(words))



# ## 12.Tokenization from a text file

# from nltk import word_tokenize
# import nltk
# nltk.download('punkt_tab')

# with open('Backup.txt')as file:
#     text = file.read()

# tokens = word_tokenize(text)
# print(tokens)





## 13.
# Complete Tokenization Program
import nltk
import string
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

text = """
Python is a powerful programming language.
It is widely used in Data Science, Machine Learing, and NLP!
"""

# Step 1: Sentence Tokenization
sentences = sent_tokenize(text)

print("Sentences:")
for sentence in sentences:
  print(sentence)

# Step 2: Word Tokenization
tokens = word_tokenize(text)

print('\nAll tokens:')
print(tokens)

## step 3: remove punctuation
words = [word for word in tokens if word not in string.punctuation]

print('\nTokens witout punctuation:')
print(words)

## step 5: Count tokens
print('\nTotal tokens:',len(tokens))
print('total words:',len(words))