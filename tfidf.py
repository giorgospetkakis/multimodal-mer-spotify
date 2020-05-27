# General imports
import glob
import numpy as np
from pathlib import Path
import re
import gensim
from collections import defaultdict
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression

# Validation packages
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score

from xml.etree import ElementTree as ET
from sklearn.feature_extraction.text import TfidfVectorizer

garbage = ['url', 'hashtag']

DIREC = Path("en")

# simple test
def get_representation_tweets(FILE):
    parsedtree = ET.parse(FILE)
    documents = parsedtree.iter("document")

    text = []
    for doc in documents:
        doc = doc.text.lower()
        d = re.split(r'\W+', doc)
        for word in d:
            if word not in garbage:
                text.append(word)
    return text


GT = DIREC / "truth.txt"
true_values = {}
f = open(GT, 'r', encoding='utf-8', errors='replace')
for line in f:
    linev = line.strip().split(":::")
    true_values[linev[0]] = linev[1]
f.close()

X = []
y = []
for FILE in DIREC.glob("*.xml"):
    # The split command below gets just the file name,
    # without the whole address. The last slicing part [:-4]
    # removes .xml from the name, so that to get the user code
    USERCODE = str(FILE).split("/")[-1][3:-4]

    # This function should return a vectorial representation of a user
    repr = get_representation_tweets(FILE)

    # We append the representation of the user to the X variable
    # and the class to the y vector
    X.append(repr)
    y.append(true_values[USERCODE])

X = np.array(X)
y = np.array(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)


class TfidfEmbeddingVectorizer(object):
    def __init__(self, word2vec):
        self.word2vec = word2vec
        self.word2weight = None
        self.dim = 50

    def fit(self, X, y):
        tfidf = TfidfVectorizer(analyzer=lambda x: x)
        tfidf.fit(X)
        max_idf = max(tfidf.idf_)
        self.word2weight = defaultdict(
            lambda: max_idf,
            [(w, tfidf.idf_[i]) for w, i in tfidf.vocabulary_.items()])

        return self

    def transform(self, X):
        return np.array([
                np.mean([self.word2vec[w] * self.word2weight[w]
                         for w in words if w in self.word2vec] or
                        [np.zeros(self.dim)], axis=0)
                for words in X
            ])

from sklearn.pipeline import Pipeline


skf = StratifiedKFold(n_splits=5)

# with open("glove.6B.50d.txt", "rb") as lines:
#     w2v = {line.split()[0]: np.array(map(float, line.split()[1:]))
#            for line in lines}



for train_index, test_index in skf.split(X, y):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index ], y[test_index]
    model = gensim.models.Word2Vec(X_train, size=50)
    w2v = dict(zip(model.wv.index2word, model.wv.vectors))
    w2v_tfidf = Pipeline([
        ("word2vec vectorizer", TfidfEmbeddingVectorizer(w2v)),
        ("extra trees", LogisticRegression(solver = 'lbfgs'))])
    w2v_tfidf.fit(X_train, y_train)
    y_pred_lr = w2v_tfidf.predict(X_test)
    print("Accuracy: ", accuracy_score(y_test, y_pred_lr))
