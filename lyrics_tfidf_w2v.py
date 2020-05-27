# General imports
import glob
import os
import re
import numpy as np
import pandas as pd
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
from sklearn.pipeline import Pipeline

from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
  
stop_words = set(stopwords.words('english')) 

def get_lyrics():
    print("Loading Lyrics...")

    pattern = re.compile(r"\[.*\]|[oaOA]+h+")
    lyrics = []
    files = os.listdir("data/lyrics/")
    idx = [int(f.split(".")[0]) for f in files]

    for f in files:
        with open("data/lyrics/" + f, "r") as lines:
            lyrics += [" ".join([w for w in word_tokenize(re.sub(pattern, "", " ".join(lines))) if not w in stop_words])]
    return np.array(lyrics), idx

def get_mood():
    print("Loading Mood Targets...")
    d = pd.read_csv("data/preprocessed/spotify-data-preprocessed.csv", ",")
    mood_vecs = [np.argmax(x) for x in d.iloc[:,-4:].to_numpy()]
    return np.array(mood_vecs)

X, idx = get_lyrics() ; y = get_mood()


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

skf = StratifiedKFold(n_splits=5)

print("Loading Word Embeddings...")
with open("data/MoodyCorpus2/lyr_cb.txt", "rb") as lines:
    w2v = {line.split()[0]: np.array(map(float, line.split()[1:]))
           for line in lines}


for train_index, test_index in skf.split(X, y):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index ], y[test_index]

    model = gensim.models.Word2Vec(X_train, size=50)

    w2v = dict(zip(model.wv.index2word, model.wv.vectors))

    w2v_tfidf = Pipeline([
        ("word2vec vectorizer", TfidfEmbeddingVectorizer(w2v)),
        ("extra trees", LogisticRegression(solver = 'newton-cg'))])

    print("Training...")
    w2v_tfidf.fit(X_train, y_train)

    y_pred_lr = w2v_tfidf.predict(X_test)
    print("Accuracy: ", accuracy_score(y_test, y_pred_lr))
