# %%
from nltk.corpus import wordnet
from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize, PunktSentenceTokenizer
import sys
import os
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import state_union
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

#useful
# tokenizing. split based on setence, words, or paragraphs
example_text = "hello this is me, how are you today? i'm doing ok"

# tokenizing sentence
print(sent_tokenize(example_text))

# tokenizing words
print(word_tokenize((example_text)))

# %%
# stop words. Filter out words that hold no meaning to save space (the, is, ... etc )
# useful
example_sent = "We are doing far more, and better, Testing than any other country in the world, and yet the media does nothing but complain. No matter how good a job is done, the same as with the Ventilators, they will never say we are doing a great job, they will only viciously gripe!"

# language english
stop_words = set(stopwords.words('english'))

# tokenize words
word_tokens = word_tokenize(example_sent)

# filter stop words
filtered_sentence = [w for w in word_tokens if not w in stop_words]

print(filtered_sentence)

# %% stemming. making words with same meaning the same write, writing, writetn, and etc...
#useful
ps = PorterStemmer()
example_words = ["python", "pythoner", "pythoning", "pythoned", "pythonly"]

# for w in example_words:
# print(ps.stem(w)

new_text = "It is important to by very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."
words = word_tokenize(example_sent)

for w in words:
    print(ps.stem(w))


# %% speech tagging. words and their meaning meaning
#useful

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

# print(tokenized)

try:
    for i in tokenized[:5]:
        words = nltk.word_tokenize(i)
        tagged = nltk.pos_tag(words)
        print(tagged)
except Exception as e:
    print(str(e))

# %% chunking. Categorize words
# useful
train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)


def process_content():
    chunked_list = []
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            print(chunked)
            # chunked.draw()
    except Exception as e:
        print(str(e))


process_content()

# %% chinking. removing chunks from the chunks above
#useful
train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)


def process_content():
    try:
        for i in tokenized[5:]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)

            chunkGram = r"""Chunk: {<.*>+}
                                    }<VB.?|IN|DT|TO>+{"""

            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            print(chunked)

    except Exception as e:
        print(str(e))


process_content()

# %% named entitiy recognition. A form of chunking, use NLTK to label chunks by people, places, locations
#useful

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)


def process_content():
    try:
        for i in tokenized[5:]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)

            # binary = True ne recognizes white house as a same named entity
            namedEnt = nltk.ne_chunk(tagged, binary=True)

            # binary = False splits names like White House into two named entities
            #namedEnt = nltk.ne_chunk(tagged, binary=False)
            print(namedEnt)
    except Exception as e:
        print(str(e))


process_content()

# %% lemmatizing with NLTK
# similar to stemming, but lemma lemma finds real word that you can find in the dictionary. pos tag used to tell it whether you want a noun, adjective, or verb. By default it gives noun


lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("python"))
print(lemmatizer.lemmatize("better", pos="a"))
print(lemmatizer.lemmatize("best", pos="a"))
print(lemmatizer.lemmatize("run"))
print(lemmatizer.lemmatize("run", 'v'))

# %% corpora with nltk. Natural language data that is included int he NLTK package


print(nltk.__file__)

# if sys.platform.startswith('win'):
# Common locations on Windows:
# path += [
#str(r'C:\nltk_data'), str(r'D:\nltk_data'), str(r'E:\nltk_data'),
#os.path.join(sys.prefix, str('nltk_data')),
#os.path.join(sys.prefix, str('lib'), str('nltk_data')),
#os.path.join(os.environ.get(str('APPDATA'), str('C:\\')), str('nltk_data'))
# ]
# else:
# Common locations on UNIX & OS X:
# path += [
# str('/usr/share/nltk_data'),
# str('/usr/local/share/nltk_data'),
# str('/usr/lib/nltk_data'),
# str('/usr/local/lib/nltk_data')
# ]


# sample text
sample = gutenberg.raw("bible-kjv.txt")

tok = sent_tokenize(sample)

for x in range(5):
    print(tok[x])
# %% WordNet lexical database for the English langauge. Use WordNet to find
# meaning of their words, synonyms, andtonyms, and etc


syns = wordnet.synsets("program")

# print(syns)

# synset
print(syns[0].name())

# just the word
print(syns[0].lemmas()[0].name())

# definition
print(syns[0].definition())

# example of word in use

print(syns[0].examples())

# making a list of synonyms and antonyms

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
print("\n")
print(synonyms)
print("\n")
print(antonyms)


#%% using wordnet to compare the noun of "ship" and "boat"  
## useful

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")
w3 = wordnet.synset("car.n.01")
w4 = wordnet.synset("cat.n.01")

print(w1.wup_similarity(w2))
print(w1.wup_similarity(w3))
print(w1.wup_similarity(w4))
# %% text classification. Some sentiment analysis 

import nltk
import random 
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

#print(documents)

random.shuffle(documents)

#print(documents[1])

all_words = []

for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)

# get 15 most common used words
print(all_words.most_common(15))
print(all_words["stupid"])