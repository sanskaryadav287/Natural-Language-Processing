

# ## 1. Read a pdf file using python

from pickletools import read_int4
from PyPDF2 import PdfReader
text = PdfReader('Pollution.pdf')
# print(len(text.pages))


# ## 2. Read First Page
# read = text.pages[0]
# print(read.extract_text())


# ## 3. Read All pages from a pdf
# reader = PdfReader('Pollution.pdf')
# for page_no,pages in enumerate(reader.pages,start= 1):
#     print(f'Page no_{page_no}_____')
#     text = pages.extract_text()
#     print(text)


# ## 4. Read a specific page
reader = PdfReader('Pollution.pdf')
# page = reader.pages[3]
# text = page.extract_text()
# print(text)


# # 5. Search for a Word in a PDF
# search_word = 'Raju'
# for page_no,page in enumerate(reader.pages,start=1):
#     text = page.extract_text()
#     if search_word.lower() in text.lower():
#         print(f'The word Found is page no {page_no}')
# else:
#     print('Word is not Found')



# ## 6. Count words in a pdf
# count = 0

# for page in reader.pages:
#     text = page.extract_text()
#     if text:
#         count += len(text.split())

# print(count)



# ## 7. Save extracted text into a txt file

# reader = PdfReader('Pollution.pdf')

# with open('PDF_text.txt','w+')as file:
#     for page_no,page in enumerate(reader.pages,start=1):
#         text = page.extract_text()
#         file.write(f'page no __{page_no}')
#         file.write(text)
#         file.seek(0)
#         text = file.read()
# print(text)


# ## 8. Copy first page into another PDF
# from PyPDF2 import PdfReader, PdfWriter

# reader = PdfReader('Pollution.pdf')
# writer = PdfWriter()

# # Copy the first page (index 0)
# writer.add_page(reader.pages[1])

# # Save into a new PDF
# with open('new.pdf', 'wb') as file:
#     writer.write(file)
#     print("Successfully created new.pdf with the first page!")

# new_pdf = PdfReader('new.pdf')
# for page_no , page in enumerate(new_pdf.pages,start=1):
#     print(f'Page No - {page_no}')
#     text = page.extract_text()
#     print(text)



# ## 9. Tokenzie words of PDF 

import nltk
from nltk.tokenize import word_tokenize

# nltk.download('punkt')
# nltk.download('punkt_tab')

# reader = PdfReader('Pollution.pdf')
# for page_no,page in enumerate(reader.pages,start=1):
#     print(f'Page No - {page_no}')
#     text = page.extract_text()
#     token = word_tokenize(text)
#     print(token)



# ## 10. Sentences Tokenize 

from nltk.tokenize import sent_tokenize
reader = PdfReader('Pollution.pdf')

# for page_no,page in enumerate(reader.pages,start=1):
#     print(f'Page No--{page_no}')
#     text = page.extract_text()
#     token = sent_tokenize(text)
#     print(token)    
#     print('='*20)


# ## 11. tokenization with Punctuation

# reader = PdfReader('Pollution.pdf')

# for page_no,page in enumerate(reader.pages,start=1):
#     print(f'page No : {page_no}')
#     text = page.extract_text()
#     token= word_tokenize(text)
#     print(token)
#     print('='*30)




# ## 12. Tokenization with numbers.

# import nltk
# from nltk.tokenize import word_tokenize
# reader = PdfReader('Pollution.pdf')

# for page_no,page in enumerate(reader.pages,start=1):
#     print(f'page No-{page_no}:--')
#     text =page.extract_text()
#     tokens = word_tokenize(text)
#     print(tokens)
#     print('-'*30)



# ## 13. Tokenization with Contraction
# reader = PdfReader('Pollution.pdf')

# for page_no, page in enumerate (reader.pages,start= 1):
#     print(f'Page-No_{page_no}--')
#     text = page.extract_text()
#     tokens = word_tokenize(text)
#     print(tokens)
#     print()
    

# ## 14.Sentences Tokenize + word Tokenize
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

# reader = PdfReader('Pollution.pdf')

# for page_no,page in enumerate(reader.pages,start = 1):
#     print(f'Page_no_{page_no}__')
#     text = page.extract_text()
#     sentences= sent_tokenize(text)
#     for sentence in sentences:
#         words = word_tokenize(sentence)
#         print(words)
#         print('-'*20)


# ## 15. Number of tokens 
# reader = PdfReader('Pollution.pdf')

# for page_no,page in enumerate(reader.pages,start=1):
#     print(f'Page_no--{page_no}')
#     text = page.extract_text()
#     tokens = word_tokenize(text)
#     print('Tokens:',tokens)
#     print(len(tokens))
#     print('--'*20)


# ## 16. Total tokens in the entire PDF (Poori PDF ke total tokens ki length)
# reader = PdfReader('Pollution.pdf')
# all_tokens =[]

# for page_no,page in enumerate(reader.pages,start= 1):
#     print(f'Page-No-{page_no}')
#     text = page.extract_text()
#     words = word_tokenize(text)
#     all_tokens.extend(words)
#     print('Total Tokens In This Page =',len(words))  
#     print('='*30)
    
# print('Total Tokens In PDF =',len(all_tokens))





# ## 17. Total Letters in PDF.

# reader = PdfReader('Pollution.pdf')
# all_letters = []

# for page_no,page in enumerate(reader.pages,start=1):
#     print(f'Page-No-{page_no}')
#     text = page.extract_text()
#     letters = [char for char in  text if char.isalpha()]
#     all_letters.extend(letters)
#     print('Letters',letters)
#     print('Total Letters In This Page =',len(letters))

# print('Total Letters In PDF =',len(all_letters))



# ## 18:Count only words
# import string 


# reader = PdfReader('Pollution.pdf')
# only_words = []
# for page_no,page in enumerate(reader.pages,start = 1):
#     text = page.extract_text()
#     tokens = word_tokenize(text)
#     words = [token for token in tokens if token not in string.punctuation]
#     print(f'Page_no{page_no}__')
#     print(words)
#     print(len(words))
#     only_words.extend(words)
#     print('='*30)

# print('Total words In PDF =',len(only_words)) 
 




# ## 19. Tokenization from a pdf file

# import nltk
# from nltk.tokenize import word_tokenize


# nltk.download('punkt_tab')

# # Open PDF file
# reader = PdfReader('Pollution.pdf')

# # Read text from all pages
# text = ""

# for page in reader.pages:
#     text += page.extract_text() or ""

# # Tokenization
# tokens = word_tokenize(text)

# print("Tokens:", tokens)
# print("Total Tokens:", len(tokens))




## 20: Lemmatization on pdf 

import spacy
from PyPDF2 import PdfReader

nlp = spacy.load('en_core_web_sm')

text = ""

for page in reader.pages:
    text += page.extract_text() or ""


doc = nlp(text)

for token in doc:
    print(token.text,'->',token.lemma_)
