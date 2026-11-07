from numpy._core.defchararray import startswith
from spacy.pipeline import lemmatizer
import spacy 
nlp = spacy.load('en_core_web_sm')



# ## 1: Basic Lemmatization
# text= ' The cats sat on the mat.'
# doc = nlp(text)
# for token in doc:
#     print(token.text,'->',token.lemma_)




# ##2 : Lemmatization Plural Nouns

# text = 'cats dogs houses cars'
# doc = nlp(text)
# for token in doc:
#     print(token.text,'-->',token.lemma_)




# ## 3: Lemmitization Verb
# text = 'playing plyed plys'
# doc = nlp(text)
# for token in doc:
#     print (token.text,'-->',token.lemma_)




# ## 4: Lemmitization different vervs froms
# text= 'The men were going to the meetings.'

# doc = nlp(text)
# for token in doc:
#     print(token.text,'-->',token.lemma_)




# ## 5: Lemmitization with a sentences
# text ='The cats are playing in the gardens' 
# doc = nlp(text)

# lemmatized_text = ' '.join(token.lemma_ for token in doc)
# print(lemmatized_text)




# ## 6: Lemmitization of regular words
# text = 'Running Ran Runner fastran fastly'
# doc = nlp(text)

# for token in doc:
#     print(token.text,'-->',token.lemma_)



# ## 7: Lemmitization based on part of speech
# text = 'I am Running fastly.'
# doc = nlp(text)

# for token in doc:
#     print(token.text,'POS',token.pos_,'Lemma:',token.lemma_)



# ## 8: Remove Puctuation and lemmaization
# text = 'The cats are playing. in the gardens!'
# doc =  nlp(text)
# words = []

# for token in doc:
#     if not token.is_punct:
#         words.append(token.lemma_)

# print(words)




# ## 9: Lemmatization with Stopwords Removal
# text ='I am here and it is a nice day.'
# doc = nlp(text)

# words = []

# for token in doc:
#     if not token.is_punct:
#         words.append(token.lemma_)

# print(words)





# ## 10: Create a Lemmatization  function
# def lemitized_text(text):
#     doc = nlp(text)
#     result = []

#     for token in doc:
#         if not token.is_punct and not token.is_stop:
#             result.append(token.lemma_)

#     return ' '.join(result)


# text = 'The student were studying in the libaray.'
# result = lemitized_text(text)
# print(result)



##   Lemmatization Using NLTK  ##
# import nltk

# nltk.download("wordnet")
# nltk.download('omw-1.4')


from nltk.stem import WordNetLemmatizer
lematize = WordNetLemmatizer()

# ## 1:Basic NLTK Lemmatization
# words = ['Cats','dogs','cars','houses']

# for word in words:
#     print(word,'->',lematize.lemmatize(word))




# ## 2: Lemmatizing verbs

# words = ['eating', 'ate', 'eaten', 'writes', 'writing', 'wrote',
#          'walking', 'walked', 'walks']

# for word in words:
#     print(word,'->',lematize.lemmatize(word,pos='v'))





# ## 3: Lemmatization Nouns
# words =[ 'dogs','cats','cows','houses']

# for word in words:
#     print(word,'__>',lematize.lemmatize(word,pos='n'))




# ## 4: Lemmatization Adjectives
# words = ['better', 'best', 'good', 'running', 'ran']

# for word in words:
#     print(word, '-->', lematize.lemmatize(word, pos='a'))




# ## 5: LEmmatization adverbs
# words = adverbs = [
#     'Now',
#     'Always',
#     'Ever',
#     'Seldom',
#     'Rarely',
#     'Gradually',
#     'Eventually',
#     'Monthly',
#     'Weekly',
#     'Yearly',
#     'Annually',
#     'Quarterly',
   
# ]

# for word in words:
#     print(word,'__>',lematize.lemmatize(word,pos='r'))





# ## 6: Irregular Verb Lemmatization
# words = ['went', 'gone', 'ate', 'eaten',
#          'wrote', 'written', 'saw', 'seen']

# for word in words:
#     print(word,'__>',lematize.lemmatize(word,pos='v'))




# ## 7: Compare Noun and Verb Lemmatization
# ## The same words can produce different results depending on it
# words = ['leaves', 'saw', 'lying', 'found', 'left']

# for word in words:
#     print('As Noun',word,'__>',lematize.lemmatize(word,pos='n'))
#     print('As Verb',word,'__>',lematize.lemmatize(word,pos='v'))




# ## 8: Lemmaization a list of a words
# words = ['playing', 'running', 'walking', 'played', 'worked', 'studied']

# for word in words:
#     if word.endswith('ing') or word.endswith('ed'):
#         lemma = lematize.lemmatize(word, pos='v')
#     else:
#         lemma = lematize.lemmatize(word, pos='n')

#     print(word, '->', lemma)




## 9: Lemmatization with Tokenization

import nltk
from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

# Download required resources
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Create lemmatizer
lemmatizer = WordNetLemmatizer()


# Function to convert POS tag into WordNet POS
def get_wordnet_pos(tag):

    if tag.startswith('J'):
        return wordnet.ADJ

    elif tag.startswith('V'):
        return wordnet.VERB

    elif tag.startswith('N'):
        return wordnet.NOUN

    elif tag.startswith('R'):
        return wordnet.ADV

    else:
        return wordnet.NOUN


# Input sentence
text = "The students are studying hard and writing beautiful stories."

# Tokenization
tokens = word_tokenize(text)

print("Tokens:", tokens)

# POS tagging
tagged_tokens = pos_tag(tokens)

print("POS Tags:", tagged_tokens)


# Lemmatization
for word, tag in tagged_tokens:

    if word.isalpha():

        pos = get_wordnet_pos(tag)

        lemma = lemmatizer.lemmatize(word, pos=pos)

        print(word, "->", lemma)











