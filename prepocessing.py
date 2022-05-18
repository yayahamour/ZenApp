import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from keras.preprocessing.text import Tokenizer
from keras.layers import TextVectorization
import tensorflow as tf


import texthero as hero
from texthero import stopwords

def nltk_tag_to_wordnet_tag(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None


def lemmatize_sentence(sentence):
    lemmatizer = WordNetLemmatizer()
    nltk_tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
    wordnet_tagged = map(lambda x: (x[0], nltk_tag_to_wordnet_tag(x[1])), nltk_tagged)
    lemmatized_sentence = []
    for word, tag in wordnet_tagged:
        if tag is None:
            lemmatized_sentence.append(word)
        else:
            lemmatized_sentence.append(lemmatizer.lemmatize(word, tag))
    return " ".join(lemmatized_sentence)

def preprocessing(data , categories = {'sadness' : 0, 'surprise' : 1, 'anger' : 2, 'fear' :3, 'happy' : 4, 'love' : 5}):
  nltk.download('averaged_perceptron_tagger')
  nltk.download('punkt')
  nltk.download('wordnet')
  nltk.download('omw-1.4')
  data["clean_text"] = hero.clean(data["Text"])
  data['clean_text'] = data['clean_text'].apply(lambda x : lemmatize_sentence(x))
  default_stopwords = stopwords.DEFAULT
  custom_stopwords = default_stopwords.union(set([]))
  data['clean_text'] = hero.remove_stopwords(data['clean_text'], custom_stopwords)
  data["target"] = data["Emotion"].map(categories)
  return(data)
