#%%
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

## tokenizing. split based on setence, words, or paragraphs
example_text = "hello this is me, how are you today? i'm doing ok"

# tokenizing sentence
print(sent_tokenize(example_text))

# tokenizing words
print(word_tokenize((example_text)))

#%%
# stop words. Filter out words that hold no meaning to save space (the, is, ... etc )
example_sent = "We are doing far more, and better, Testing than any other country in the world, and yet the media does nothing but complain. No matter how good a job is done, the same as with the Ventilators, they will never say we are doing a great job, they will only viciously gripe!"

#language english
stop_words = set(stopwords.words('english'))

#tokenize words 
word_tokens= word_tokenize(example_sent)

#filter stop words
filtered_sentence = [w for w in word_tokens if not w in stop_words]

print(filtered_sentence)

# %% stemming. making words with same meaning the same write, writing, writetn, and etc...

ps = PorterStemmer()
example_words = ["python","pythoner","pythoning","pythoned","pythonly"]

##for w in example_words:
    ##print(ps.stem(w)

new_text = "It is important to by very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."
words = word_tokenize(example_sent)

for w in words:
    print(ps.stem(w))
    

# %% speech tagging. words and their meaning meaning
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer


train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

##print(tokenized)

try: 
    for i in tokenized[:5]:
        words = nltk.word_tokenize(i)
        tagged = nltk.pos_tag(words)
        print(tagged)
except Exception as e:
    print(str(e))
