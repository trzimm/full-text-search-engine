import re
import nltk

#nltk.download('wordnet')
sno = nltk.stem.SnowballStemmer('english')
lemma = nltk.wordnet.WordNetLemmatizer()
stopwords = ["a", "and", "be", "have", "i", "in", "of", "that", "the", "to", "it", "be", "by", "or", "is", "for", "on", "not", "with", "he", "as", "you"]

def analyze(text):
    tokens = tokenize(text)
    tokens = lowercaseFilter(tokens)
    tokens = stopwordFilter(tokens)
    tokens = lemmatizerFilter(tokens)
    return tokens

def tokenize(text):
    try:
        return re.findall(r"[\w']+", text)
    except:
        return []

def lowercaseFilter(tokens):
    for i in range(len(tokens)):
        item = tokens[i]
        tokens[i] = item.lower()
    return tokens

def stopwordFilter(tokens):
    for token in tokens:
        if token in stopwords:
            tokens.remove(token)
    return tokens


def lemmatizerFilter(tokens):
    for i in range(len(tokens)):
        item = tokens[i]
        tokens[i] =  lemma.lemmatize(item)
    return tokens